from keras.preprocessing.image import load_img
import os

def get_picture(image_path):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")
    return load_img(image_path, color_mode='rgba', target_size=(254, 254))
