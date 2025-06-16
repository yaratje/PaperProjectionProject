import cv2
import numpy as np
import time
from datetime import datetime, timedelta

from smartWatchSignal import databse_setup, trigger_alert
from dectectHand import detect_hand_and_gesture, point_inside_polygon
from navigation_config import NAV_CONFIG          # <— import our data‐driven config
from navigation import get_projector_screen         # unchanged
from calender import add_event


databse_setup()

# ArUco / marker‐overlays logic (“last_seen_markers”, H, detector, etc) stays exactly as you had it.

last_seen_markers = {}
MARKER_TIMEOUT = 10
H = np.load("homography_matrix.npy")

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

# Point-at-button cooldown
last_trigger_time = 0
COOLDOWN = 0.3   # you can tune this if you want very fast nav

# Start “current screen” on “main”
current_screen_key = "main_1_1"
debug_window_name = "Debug View"

abs_polygons = []
screen_cfg = None


projector = get_projector_screen()
proj_w, proj_h = projector.width, projector.height
proj_x, proj_y = projector.x, projector.y

win_name = "Projector"
cv2.namedWindow(win_name, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(win_name, proj_x, proj_y)
cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cap = cv2.VideoCapture(1)

def rel_to_abs_poly(poly_rel, width, height):
    """
    Convert a polygon given in normalized coords [0..1] to absolute pixel coords.
    poly_rel is a list of [x_norm, y_norm] points.
    """
    return [(int(x*width), int(y*height)) for (x, y) in poly_rel]

def draw_region(frame, polygon_abs, label):
    """
    Draw a semi-transparent filled polygon with a red border and white label at its center.
    """
    pts = np.array(polygon_abs, np.int32).reshape((-1, 1, 2))
    # Draw filled red with alpha
    overlay = frame.copy()
    cv2.fillPoly(overlay, [pts], color=(0, 0, 255))
    alpha = 0.3
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
    # Draw border
    cv2.polylines(frame, [pts], isClosed=True, color=(0, 0, 255), thickness=2)
    # Put label at centroid
    cx = int(np.mean([p[0] for p in polygon_abs]))
    cy = int(np.mean([p[1] for p in polygon_abs]))
    cv2.putText(frame, label, (cx - len(label)*6, cy + 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)



prev_hand_state = "unknown"
click_triggered = False

def on_debug_click(event, x, y, flags, param):
    global current_screen_key, last_trigger_time
    if event == cv2.EVENT_LBUTTONDOWN:
        # abs_polygons must be accessible here too; we'll pass it via `param`
        
        for (poly_abs, target_screen) in abs_polygons:
            if point_inside_polygon((x, y), poly_abs):
                print(f"[DEBUG] Mouse clicked: {current_screen_key} → {target_screen}")
                current_screen_key = target_screen
                last_trigger_time = time.time()
                break


cv2.namedWindow(debug_window_name)

cv2.setMouseCallback(debug_window_name, on_debug_click)


while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # 1) Run marker detection as before
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    corners, ids, _ = detector.detectMarkers(gray)

    seen_ids = set()
    pinch, is_pointing, hand_state = detect_hand_and_gesture(rgb, frame)

    click_triggered = False
    if prev_hand_state == "open" and hand_state == "closed":
        click_triggered = True
    prev_hand_state = hand_state

    # Update your ArUco cache (last_seen_markers) exactly as you already do...
    if ids is not None:
        for marker_corners, marker_id in zip(corners, ids.flatten()):
            seen_ids.add(marker_id)
            if marker_id in last_seen_markers:
                last_seen_markers[marker_id]["corners"] = marker_corners[0].astype(np.float32)
                last_seen_markers[marker_id]["frames_left"] = MARKER_TIMEOUT
            else:
                last_seen_markers[marker_id] = {
                    "corners": marker_corners[0].astype(np.float32),
                    "frames_left": MARKER_TIMEOUT
                }

    for mid in list(last_seen_markers.keys()):
        if mid in seen_ids:
            # we already updated in the loop above—so just reset timeout
            last_seen_markers[mid]["frames_left"] = MARKER_TIMEOUT
        else:
            last_seen_markers[mid]["frames_left"] -= 1
            if last_seen_markers[mid]["frames_left"] <= 0:
                del last_seen_markers[mid]

    # 2) Load the current screen image (and resize)
    screen_cfg = NAV_CONFIG[current_screen_key]
    base_img = cv2.imread(screen_cfg["image_path"])
    if base_img is None:
        # If the image fails to load, fill black
        projector_img = np.zeros((proj_h, proj_w, 3), dtype=np.uint8)
        cv2.putText(projector_img, f"Missing: {screen_cfg['image_path']}",
                    (50, proj_h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
    else:
        projector_img = cv2.resize(base_img, (proj_w, proj_h))

    # 3) Draw all hotspots / buttons for this screen
    regions = screen_cfg.get("regions", [])
    abs_polygons = []    # store these so we can check pointer collisions
    for region in regions:
        poly_abs = rel_to_abs_poly(region["polygon_rel"], proj_w, proj_h)
        draw_region(projector_img, poly_abs, region["label"])
        abs_polygons.append((poly_abs, region["target"]))

    # 4) Draw your ArUco/machine overlay (green polygons + labels) on top
    for marker_id, marker_data in last_seen_markers.items():
        # Take the most recently updated corners
        pts = marker_data["corners"].reshape(-1, 1, 2).astype(np.float32)
        projected_pts = cv2.perspectiveTransform(pts, H)
        projected_pts_int = projected_pts.astype(int)
        # Fill green polygon
        cv2.fillPoly(projector_img, [projected_pts_int], (0, 255, 0))
        # Put “Machine X” label at its centroid
        center = np.mean(projected_pts.reshape(-1, 2), axis=0).astype(int)
        label = f"Machine {marker_id}"
        cv2.putText(projector_img, label, (center[0] - 30, center[1] + 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)


    cv2.setMouseCallback(debug_window_name, on_debug_click, param=(abs_polygons, screen_cfg))


    # 5) Check pointing & navigation
    #print(click_triggered, hand_state, pinch)
    if click_triggered and pinch is not None:
        # 1) Map pinch center to projector coords
        pinch_proj = cv2.perspectiveTransform(
            np.array([[pinch]], dtype=np.float32), H
        )[0,0].astype(int)
        cx, cy = int(pinch_proj[0]), int(pinch_proj[1])

        # 2) Draw the pinch circle for debugging
        CLICK_RADIUS = 100  # adjust for a bigger/smaller hit‐area
        cv2.circle(projector_img, (cx, cy), CLICK_RADIUS, (255,255,0), 3)

        # 3) Build a click‐mask (binary image) for that circle
        click_mask = np.zeros((proj_h, proj_w), dtype=np.uint8)
        cv2.circle(click_mask, (cx, cy), CLICK_RADIUS, 255, -1)

        # 4) For each region, build a mask and measure overlap
        best_target = None
        best_area = 0
        for (poly_abs, target_screen) in abs_polygons:
            # polygon mask
            poly_mask = np.zeros_like(click_mask)
            cv2.fillPoly(poly_mask, [np.array(poly_abs, np.int32)], 255)

            # overlap area
            overlap = cv2.bitwise_and(click_mask, poly_mask)
            area = cv2.countNonZero(overlap)

            if area > best_area:
                best_area = area
                best_target = target_screen

        now = time.time()
        if best_target is not None and (now - last_trigger_time) > COOLDOWN:
            print(f"Navigating: {current_screen_key} → {best_target}  (overlap {best_area}px²)")
            if best_target == "not_calender":
                print("trying to add event")
                add_event("Fix machine 1", datetime.time() + timedelta(days=2), 30)
            elif best_target == "not_green":
                trigger_alert("bob")
            else:
                current_screen_key = best_target
            last_trigger_time = now

    # 6) Show everything
    cv2.imshow(win_name, projector_img)
    cv2.imshow("Camera", frame)

    cv2.imshow(debug_window_name, projector_img)
    cv2.setMouseCallback(debug_window_name, on_debug_click)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC to quit
        break

    if key == ord('1'):
        current_screen_key = "main_1_1"
    elif key == ord('2'):
        current_screen_key = "main_2_1"
    elif key == ord('3'):
        current_screen_key = "main_3_1"
    



cap.release()
cv2.destroyAllWindows()