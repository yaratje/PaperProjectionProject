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
def is_open_hand(landmarks):
    # Only require index + middle to be extended
    def y(id): return landmarks[id].y
    return (y(8) < y(6)) and (y(12) < y(10))

def is_closed_hand(landmarks):
    # Only require index + middle to be folded
    def y(id): return landmarks[id].y
    return (y(8) > y(6)) and (y(12) > y(10))

last_hand_state = "unknown"


def detect_hand_and_gesture(frame_rgb, frame_bgr):
    
    global last_hand_state
    result = hands.process(frame_rgb)
    h, w, _ = frame_bgr.shape
    pinch_px = None
    index_finger_px = None
    pointing = False
    hand_state = last_hand_state  # start from previous

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        mp_drawing.draw_landmarks(frame_bgr, hand, mp_hands.HAND_CONNECTIONS)
        lm = hand.landmark

        index_finger_px = (int(lm[8].x * w), int(lm[8].y * h))
        thumb_finger_px = (int(lm[4].x * w), int(lm[4].y * h))
    # midpoint between index tip (8) and thumb tip (4)
        pinch_px = (
        int((lm[8].x + lm[4].x) / 2 * w),
        int((lm[8].y + lm[4].y) / 2 * h),
)
        if is_pointing(lm): pointing = True

        # only switch if we detect a definite open/closed
        if is_open_hand(lm):
            hand_state = "open"
        elif is_closed_hand(lm):
            hand_state = "closed"
        # else leave hand_state as last_hand_state

    last_hand_state = hand_state
    return pinch_px, pointing, hand_state

#ja dis zon beetje zon kan allebei function miss beter in cameramain of in een random utils ofzo
def point_inside_polygon(point, polygon):
    return cv2.pointPolygonTest(np.array(polygon, dtype=np.int32), point, False) >= 0