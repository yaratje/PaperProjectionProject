import cv2
import cv2.aruco as aruco
import os

#params
output_folder = 'markers'
marker_ids = [0, 1,2,4]  #idk how many do we want?
marker_size = 200
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

#generate and save
for marker_id in marker_ids:
    marker_image = aruco.generateImageMarker(dictionary, marker_id, marker_size)
    file_path = os.path.join(output_folder, f'marker_{marker_id}.png')
    cv2.imwrite(file_path, marker_image)
    aruco.generateImageMarker