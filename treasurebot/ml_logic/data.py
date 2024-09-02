import os
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def get_picture(name):
    # Construct the absolute path to the image
    image_path = os.path.join(
        '/home/belalsajal/code/belalsajal/TreasureBot3000/treasurebot/web_interface/bg_images', name
    )

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
