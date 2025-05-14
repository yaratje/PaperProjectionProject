import cv2
import cv2.aruco as aruco

#id naar name mapping
marker_names = {
    0: "paper machine 1",
    1: "paper machine 2",
    #enzovoort met betere namen
}

#auto vind een werkende camera backup
def find_working_camera(max_id=5):
    for cam_id in range(max_id):
        cap = cv2.VideoCapture(cam_id)
        if cap.isOpened():
            return cap, cam_id
        cap.release()
    return None, -1

# Load the dictionary used to generate the markers
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

#als de ondere niet werkt detect wat anders maar hij pakt de eerste dus als je build in cam + usb dan pakt ie de verkeerde
#cap, cam_id = find_working_camera()

cap = cv2.VideoCapture(1)

if cap is None:
    print("no camera")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("frame could not be loaded :(")
        break

    #grayscale voor betere detection,
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    corners, ids, rejected = aruco.detectMarkers(gray, dictionary)

    if ids is not None:
        for i, corner in enumerate(corners):
            id = int(ids[i])
            name = marker_names.get(id, f"Unknown {id}")

            #box marker
            int_corners = corner[0].astype(int)
            cv2.polylines(frame, [int_corners], isClosed=True, color=(0, 255, 0), thickness=2)

            #geeft marker de goeie naam
            x, y = int_corners[0][0], int_corners[0][1]
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.8, (0, 255, 0), 2, cv2.LINE_AA)

    #print frame
    cv2.imshow("ArUco Marker Detection", frame)

    #stop
    key = cv2.waitKey(1)
    if key == 27:  #ESCAPE
        break

cap.release()
cv2.destroyAllWindows()
