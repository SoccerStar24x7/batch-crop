import cv2
import numpy as np

image = "YOUR IMAGE PATH"

img = cv2.imread(image)
print(img.shape) 
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped_image = img["INPUT SLICING CROP INFO (SEE README)"] # Slicing to crop the image
 
# Display the cropped image
cv2.imshow("cropped", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 