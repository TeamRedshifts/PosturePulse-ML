# Write a script to take all the jpegs in the folder and create horizontally flipped images of the same

import os
import cv2
import numpy as np

FOLDER_NAME = 'single_leg_raise'

def flip_images(images_folder):
    for image_name in os.listdir(images_folder):
        if not image_name.endswith('.jpg') and not image_name.endswith('.jpeg') and not image_name.endswith('.png'):
            continue
        image_path = os.path.join(images_folder, image_name)
        image = cv2.imread(image_path)
        flipped_image = cv2.flip(image, 1)
        flipped_image_path = os.path.join(images_folder, 'flipped', image_name.split('.')[0] + '_flipped.jpg')
        # flipped_image_path = os.path.join(images_folder,'_flipped.jpg')
        print("Saving", flipped_image_path)
        cv2.imwrite(flipped_image_path, flipped_image)

flip_images(FOLDER_NAME)
