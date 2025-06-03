import cv2
import numpy as np

# Load your image
image_path = 'nav/machine1_1.png'
img = cv2.imread(image_path)
if img is None:
    raise FileNotFoundError(f"Could not load image at {image_path}")

img_copy = img.copy()
drawing = False
current_polygon = []
polygons = []

height, width, _ = img.shape

def format_normalized_polygon(polygon):
    lines = []
    for (x, y) in polygon:
        nx = round(x / width, 4)
        ny = round(y / height, 4)
        lines.append(f"[{nx},  {ny}],")
    return "\n".join(lines)

def mouse_callback(event, x, y, flags, param):
    global drawing, current_polygon, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        current_polygon.append((x, y))
        cv2.circle(img_copy, (x, y), 4, (0, 0, 255), -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        if len(current_polygon) >= 3:
            polygons.append(current_polygon.copy())
            print(f"\n✅ Saved Polygon {len(polygons)}:")
            print(format_normalized_polygon(current_polygon))
            cv2.polylines(img_copy, [np.array(current_polygon)], isClosed=True, color=(0, 255, 0), thickness=2)
        else:
            print("⚠️ Polygon needs at least 3 points.")
        current_polygon.clear()

cv2.namedWindow("Draw Polygons")
cv2.setMouseCallback("Draw Polygons", mouse_callback)

print("🖱️ Left click to add points.\n🖱️ Right click to finish a polygon.\n⎋ Press ESC to quit.\n")

while True:
    cv2.imshow("Draw Polygons", img_copy)
    key = cv2.waitKey(1)

    if key == 27:  # ESC
        break

cv2.destroyAllWindows()
