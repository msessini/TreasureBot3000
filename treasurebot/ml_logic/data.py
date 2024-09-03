import os
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def get_picture(name):
    # Construct the absolute path to the image
    current_dir = os.path.dirname(__file__)
    image_path = os.path.abspath(os.path.join(current_dir, '..', 'web_interface', 'bg_images', name))

    print(f"Attempting to load image from: {image_path}")

    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return None

    # Load the image
    try:
        picture = Image.open(image_path)
        picture = picture.resize((254, 254))  # Resize image if necessary
        print("Image loaded successfully")
        return picture
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
