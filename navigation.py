folder = "nav/"
import cv2
from screeninfo import get_monitors

sections = ["main", "machine1", "machine2"]


def get_projector_screen():
    monitors = get_monitors()
    return monitors[-1]

def get_nav(section, number):
    
    projector = get_projector_screen()
    proj_w, proj_h = projector.width, projector.height
    projector_img = cv2.imread(folder + sections[section] + number + ".png")
    projector_img = cv2.resize(projector_img, (proj_w, proj_h))
    return projector_img

