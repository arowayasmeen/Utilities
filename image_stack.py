import os
import numpy as np
import cv2

raw_image_dir =         "/home/asus/Projects/Work/PaddleOCR+Tesseract/Fresh/NID/image-processor-pipeline-outputs/grayscaled"
processed_image_dir =   "/home/asus/Projects/Work/PaddleOCR+Tesseract/Fresh/NID/image-processor-pipeline-outputs/all"
output_dir =            "/home/asus/Projects/Work/PaddleOCR+Tesseract/Fresh/NID/image-processor-pipeline-outputs/all-raw"

for image_name in os.listdir(raw_image_dir):
    image_1_path = os.path.join(raw_image_dir, image_name)
    image_2_path = os.path.join(processed_image_dir, image_name)
    out_path = os.path.join(output_dir,image_name)
    image_1 = cv2.imread(image_1_path)
    image_2 = cv2.imread(image_2_path)
    image_out = np.hstack([image_1, image_2])
    cv2.imwrite(out_path, image_out)