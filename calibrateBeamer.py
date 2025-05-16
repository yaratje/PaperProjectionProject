from screeninfo import get_monitors

for i, monitor in enumerate(get_monitors()):
    print(f"Monitor {i}: {monitor}")

import cv2
import numpy as np
from screeninfo import get_monitors

#projector-space points
def get_projector_points(width, height):
    margin = 100
    return np.array([
        [margin, margin],
        [width - margin, margin],
        [width - margin, height - margin],
        [margin, height - margin]
    ], dtype=np.float32)

#get projector. Not sure how this will turn out :()
def get_projector_monitor():
    monitors = get_monitors()
    return monitors[-1]  #assume its the last one ig

#click the 4 corners
def collect_camera_points(frame, num_points=4):
    points = []

    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(points) < num_points:
                points.append([x, y])

    clone = frame.copy()
    cv2.namedWindow("Click projected points (Camera View)")
    cv2.setMouseCallback("Click projected points (Camera View)", click_event)

    while len(points) < num_points:
        display = clone.copy()
        for p in points:
            cv2.circle(display, tuple(p), 5, (0, 0, 255), -1)
        cv2.imshow("Click projected points (Camera View)", display)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyWindow("Click projected points (Camera View)")
    return np.array(points, dtype=np.float32)

def main():
    projector = get_projector_monitor()
    proj_w, proj_h = projector.width, projector.height
    proj_x, proj_y = projector.x, projector.y

    #black + 4 white
    projected_image = np.zeros((proj_h, proj_w, 3), dtype=np.uint8)
    projector_points = get_projector_points(proj_w, proj_h)
    for pt in projector_points:
        cv2.circle(projected_image, tuple(pt.astype(int)), 20, (255, 255, 255), -1)

    #project
    win_name = "Projector"
    cv2.namedWindow(win_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(win_name, proj_x, proj_y)
    cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(win_name, projected_image)
    print("Projecting points")

    cap = cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow("Camera View", frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break

    # \Pause, collect clicks
    _, cam_frame = cap.read()
    camera_points = collect_camera_points(cam_frame)

    #homography
    H, _ = cv2.findHomography(camera_points, projector_points)
    print("Homography matrix:")
    print(H)
    np.save("homography_matrix.npy", H)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()