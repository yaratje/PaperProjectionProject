import cv2
import mediapipe as mp
import numpy as np


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.6)

#wat random bounderaries diek gepikt heb
def is_pointing(landmarks):
    def y(id): return landmarks[id].y
    index_extended = y(8) < y(6)
    middle_folded = y(12) > y(10)
    ring_folded = y(16) > y(14)
    pinky_folded = y(20) > y(18)
    return index_extended and middle_folded and ring_folded and pinky_folded

#werkt niet alleen met 1 hand in beeld daarna gaat ie grr
def detect_hand_and_index(frame_rgb, frame_bgr):
    result = hands.process(frame_rgb)
    h, w, _ = frame_bgr.shape
    index_finger_px = None
    pointing = False

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame_bgr, hand, mp_hands.HAND_CONNECTIONS)
            if is_pointing(hand.landmark):
                pointing = True
                lm = hand.landmark
                index_finger_px = (int(lm[8].x * w), int(lm[8].y * h))
                break
    return index_finger_px, pointing

#ja dis zon beetje zon kan allebei function miss beter in cameramain of in een random utils ofzo
def point_inside_polygon(point, polygon):
    return cv2.pointPolygonTest(np.array(polygon, dtype=np.int32), point, False) >= 0