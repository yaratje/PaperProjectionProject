import cv2
import cv2.aruco as aruco
import numpy as np

#id naar name mapping
marker_names = {
    0: "paper machine 1",
    1: "paper machine 2",
    2: "paper machine 3",
    3: "paper machine 4",
    #enzovoort met betere namen
}

#dit is de marker naar id ding library
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

#doe recognition en map het naar een naam
def detect_markers(frame_gray):
    corners, ids, _ = aruco.detectMarkers(frame_gray, dictionary)
    detections = []
    if ids is not None:
        for i, corner in enumerate(corners):
            marker_id = int(ids[i])
            polygon = corner[0].astype(int)
            name = marker_names.get(marker_id, f"Unknown {marker_id}")
            detections.append({'id': marker_id, 'name': name, 'polygon': polygon})
    return detections

#voor de duidelijkheid draw een box + zet naam erbij
def draw_markers(frame, detections):
    for marker in detections:
        cv2.polylines(frame, [marker['polygon']], True, (0, 255, 0), 2)
        cv2.putText(frame, marker['name'], tuple(marker['polygon'][0]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def marker_center(polygon):
    return np.mean(polygon, axis=0).astype(int)