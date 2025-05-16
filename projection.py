import cv2
import numpy as np
from screeninfo import get_monitors

last_seen_markers = {}
MARKER_TIMEOUT = 10  

H = np.load("homography_matrix.npy")

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)


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

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = detector.detectMarkers(gray)

    seen_ids = set()

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

    cv2.imshow(win_name, projector_img)

    #debug camera
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:  #escape
        break

cap.release()
cv2.destroyAllWindows()
