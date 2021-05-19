#This code takes images from two different directories and stacks them side by side
#Both images have the same file name in two different directories

import os
import numpy as np
import cv2

image_1_dir =   "first/directory"
image_2_dir =   "second/directory/"
output_dir =    "output/directory"

for image_name in os.listdir(image_1_dir):
    image_1_path = os.path.join(image_1_dir, image_name)
    image_2_path = os.path.join(image_2_dir, image_name)
    out_path = os.path.join(output_dir,image_name)
    image_1 = cv2.imread(image_1_path)
    image_2 = cv2.imread(image_2_path)
    image_out = np.hstack([image_1, image_2])
    cv2.imwrite(out_path, image_out)
