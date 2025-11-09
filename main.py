import os

try:
    import cv2
except ModuleNotFoundError:
    print("OpenCV dependancy not installed. Installing now...")
    os.system("pip install opencv-python")


def crop_images(folder_path):

    for filename in os.listdir(folder_path):

        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):  # Check for common image extensions
            image_path = os.path.join(folder_path, filename)
            img = cv2.imread(image_path)
            
            try:
                cropped_image = img["ADD SLICING INFO (SEE GITHUB README)"] # Slicing to crop the image. REMOVE THE QUOTES_________________________________

            except IndexError:
                print("FILL IN YOUR SLICING INFO!! CHECK README!")
                print("Script will exit now.")
                exit(1)

            cv2.imwrite(image_path, cropped_image)


def main():

    folder_path = input("Folder Path: ")  # get folder path

    print("Friendly Reminder: make sure the slicing info is right!")

    crop_images(folder_path)  # call the function to crop images


main()
