from tensorflow.keras.preprocessing.image import load_img
import os

image_path = '/home/belalsajal/code/belalsajal/TreasureBot3000/treasurebot/web_interface/bg_images/yellow_bin.png'

print(f"Testing image loading from: {image_path}")

if os.path.exists(image_path):
    try:
        image = load_img(image_path, target_size=(254, 254))
        print("Image loaded successfully")
    except Exception as e:
        print(f"Error loading image: {e}")
else:
    print("Image not found")
