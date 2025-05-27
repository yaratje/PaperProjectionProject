import cv2
import numpy as np
from screeninfo import get_monitors
from smartWatchSignal import databse_setup, trigger_alert
from dectectHand import detect_hand_and_index, point_inside_polygon
import time

databse_setup()

last_seen_markers = {}
MARKER_TIMEOUT = 10  

H = np.load("homography_matrix.npy")

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

# Button 1: "user123" (top-right)
button_user123_polygon = [
    (540, 40),   # top-left
    (640, 40),   # top-right
    (640, 100),  # bottom-right
    (540, 100)   # bottom-left
]

# Button 2: "bob" (just below button 1)
button_bob_polygon = [
    (540, 110),  # top-left
    (640, 110),  # top-right
    (640, 170),  # bottom-right
    (540, 170)   # bottom-left
]

last_trigger_time = 0
COOLDOWN = 20  # seconds

def get_projector_screen():
    monitors = get_monitors()
    return monitors[-1]

projector = get_projector_screen()
proj_w, proj_h = projector.width, projector.height
proj_x, proj_y = projector.x, projector.y

win_name = "Projector"
cv2.namedWindow(win_name, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(win_name, proj_x, proj_y)
cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cap = cv2.VideoCapture(1)


def map_point(point, H):
    pts = np.array([[point]], dtype=np.float32)  # shape (1,1,2)
    projected = cv2.perspectiveTransform(pts, H)  # shape (1,1,2)
    return tuple(projected[0,0])

def make_button_polygon(proj_w, proj_h, right_margin_ratio=0.05, top_margin_ratio=0.05,
                        width_ratio=0.2, height_ratio=0.08):
    x_right = int(proj_w * (1 - right_margin_ratio))
    x_left = x_right - int(proj_w * width_ratio)
    y_top = int(proj_h * top_margin_ratio)
    y_bottom = y_top + int(proj_h * height_ratio)
    return [(x_left, y_top), (x_right, y_top), (x_right, y_bottom), (x_left, y_bottom)]

def draw_button(frame, polygon, label):
    pts = np.array(polygon, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(frame, [pts], isClosed=True, color=(0,0,255), thickness=2)  # red border
    # Fill a little transparent red? Or just filled polygon:
    overlay = frame.copy()
    cv2.fillPoly(overlay, [pts], color=(0,0,255))
    alpha = 0.3
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
    # Put label inside
    cx = int(np.mean([p[0] for p in polygon]))
    cy = int(np.mean([p[1] for p in polygon]))
    cv2.putText(frame, label, (cx-30, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)


while True:
    ret, frame = cap.read()
    if not ret:
        continue

 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    corners, ids, _ = detector.detectMarkers(gray)

    seen_ids = set()

    index_finger, is_pointing = detect_hand_and_index(rgb, frame)

    # Update marker cache with current detections
    if ids is not None:
        for marker_corners, marker_id in zip(corners, ids.flatten()):
            seen_ids.add(marker_id)
            if marker_id in last_seen_markers:
            # Marker already known: update its position and reset timeout
                last_seen_markers[marker_id]["corners"] = marker_corners[0].astype(np.float32)
                last_seen_markers[marker_id]["frames_left"] = MARKER_TIMEOUT
            else:
                # New marker
                last_seen_markers[marker_id] = {
                    "corners": marker_corners[0].astype(np.float32),
                    "frames_left": MARKER_TIMEOUT
                }

    # Decrease timer for unseen markers
    for marker_id in list(last_seen_markers.keys()):
        if marker_id in seen_ids:
            # Update the corner position even if already in cache
            last_seen_markers[marker_id]["corners"] = marker_corners[0].astype(np.float32)
            last_seen_markers[marker_id]["frames_left"] = MARKER_TIMEOUT
        else:
            # Marker not seen this frame, decrease lifetime
            last_seen_markers[marker_id]["frames_left"] -= 1

    projector_img = np.zeros((proj_h, proj_w, 3), dtype=np.uint8)
    button_user123_polygon = make_button_polygon(proj_w, proj_h, right_margin_ratio=0.05, top_margin_ratio=0.05)
    button_bob_polygon = make_button_polygon(proj_w, proj_h, right_margin_ratio=0.05, top_margin_ratio=0.05 + 0.1)  # 10% lower on screen
    
    draw_button(projector_img, button_user123_polygon, "User123")
    draw_button(projector_img, button_bob_polygon, "Bob")
    
    for marker_id, marker_data in last_seen_markers.items():
        pts = marker_corners[0].astype(np.float32).reshape(-1, 1, 2)
        projected_pts = cv2.perspectiveTransform(pts, H)
        projected_pts_int = projected_pts.astype(int)

            #green square
        cv2.fillPoly(projector_img, [projected_pts_int], (0, 255, 0))

            #+name
        center = np.mean(projected_pts.reshape(-1, 2), axis=0).astype(int)
        label = f"Machine {marker_id}"
        cv2.putText(projector_img, label, center, cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

    if is_pointing and index_finger:
        index_proj = map_point(index_finger, H)
        for marker in last_seen_markers.items():
            if point_inside_polygon(index_proj, marker['polygon']):
                print("je raakte", marker['name'])
                break
        
        if point_inside_polygon(index_proj, button_user123_polygon):
            now = time.time()
            if now - last_trigger_time > COOLDOWN:
                print("triggered1")
                trigger_alert("user123")
                last_trigger_time = now

        elif point_inside_polygon(index_proj, button_bob_polygon):
            now = time.time()
            if now - last_trigger_time > COOLDOWN:
                print("triggered2")
                trigger_alert("bob")
                last_trigger_time = now

    cv2.imshow(win_name, projector_img)

    #debug camera
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:  #escape
        break

cap.release()
cv2.destroyAllWindows()
