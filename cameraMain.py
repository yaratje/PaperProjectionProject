import cv2
from detectMarkers import detect_markers, draw_markers
from dectectHand import detect_hand_and_index, point_inside_polygon


#auto vind een werkende camera backup
def find_working_camera(max_id=5):
    for cam_id in range(max_id):
        cap = cv2.VideoCapture(cam_id)
        if cap.isOpened():
            return cap, cam_id
        cap.release()
    return None, -1

#als de ondere niet werkt detect wat anders maar hij pakt de eerste dus als je build in cam + usb dan pakt ie de verkeerde
#cap, cam_id = find_working_camera()

cap = cv2.VideoCapture(1)

if cap is None:
    print("no camera")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect markers
    markers = detect_markers(gray)
    draw_markers(frame, markers)

    # Detect hand
    index_finger, is_pointing = detect_hand_and_index(rgb, frame)

    # Check if finger touches marker
    if is_pointing and index_finger:
        for marker in markers:
            if point_inside_polygon(index_finger, marker['polygon']):
                print("je raakte", marker['name'])
                break

    cv2.imshow("Interaction", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
