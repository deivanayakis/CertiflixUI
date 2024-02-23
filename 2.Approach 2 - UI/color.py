import math
import numpy
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976
def rgb_to_lab(rgb):
    # Assuming rgb is a list of [R, G, B]
    rgb_normalized = [val / 255.0 for val in rgb]
    lab = LabColor(rgb_normalized[0], rgb_normalized[1], rgb_normalized[2])
    return lab
l=['yellow','orange','violet','light green','brown','pink','sky blue','purple','red','green','blue','white','black','golden']
color_mapping = {
        "yellow": [255, 255, 0],
        "orange": [255, 165, 0],
        "violet": [238, 130, 238],
        "light Green": [144, 238, 144],
         "brown": [165, 42, 42],
        "pink": [255, 192, 203],
        "sky Blue": [135, 206, 250],
        "purple": [128, 0, 128],
        "red":[255, 0, 0],
        "green":[0, 255, 0],
        "blue":[0, 0, 255],
        "white":[255, 255, 255],
        "black":[0, 0, 0],
        "golden": [255, 215, 0]
    }
