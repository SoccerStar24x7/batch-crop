import cv2
import numpy as np
import os

folder_path = "path/to/your/folder"  # Replace with your folder path

for filename in os.listdir(folder_path):

    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):  # Check for common image extensions
        image_path = os.path.join(folder_path, filename)
        img = cv2.imread(image_path)

        print(img.shape)
        cropped_image = img["INPUT SLICING CROP INFO (SEE README)"] # Slicing to crop the image
        cv2.imwrite(image_path, cropped_image)

        cv2.imshow("cropped", cropped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows() # Close the display window
