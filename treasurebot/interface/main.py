from PIL import Image
import os

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

def generate_output(class_name):

    # Define the paths to the images
    image_paths = {
        "DrinkCans": "yellow_bin.png",
        "GlassBottles": "glass_bin.png",
        "PlasticBottles": "yellow_bin.png",
        "Aluminium": "yellow_bin.png",
        "Glass": "glass_bin.png",
        "Plastic": "yellow_bin.png",
        "Paperboard": "blue_bin.png",
        "Organic": "brown_bin.png"
    }

    topText = ""
    picture = None
    extraText = ""

    if class_name == "DrinkCans":
        topText = "This is a drinking can! It goes to the yellow bin (Wertstofftonne)."
        picture = get_picture(image_paths[class_name])
        extraText = "Remember to check if your can has a deposit before throwing it away."

    elif class_name == "GlassBottles":
        topText = "This is a glass bottle! It goes to the glass recycling bin (Glastonne)."
        picture = get_picture(image_paths[class_name])
        extraText = "Remember to check if your bottle has a deposit before throwing it away."

    elif class_name == "PlasticBottles":
        topText = "This is a plastic bottle! It goes to the yellow bin (Wertstofftonne)."
        picture = get_picture(image_paths[class_name])
        extraText = "Remember to check if your bottle has a deposit before throwing it away."

    elif class_name == "Aluminium":
        topText = "This is metal! It goes to the yellow bin (Wertstofftonne)."
        picture = get_picture(image_paths[class_name])
        extraText = ""

    elif class_name == "Glass":
        topText = "This is glass! It goes to the glass recycling bin (Glastonne)."
        picture = get_picture(image_paths[class_name])
        extraText = ""

    elif class_name == "Plastic":
        topText = "This is plastic! It goes to the yellow bin (Wertstofftonne)."
        picture = get_picture(image_paths[class_name])
        extraText = ""

    elif class_name == "Paperboard":
        topText = "This is paper! It goes to the blue bin (Altpapier)."
        picture = get_picture(image_paths[class_name])
        extraText = ""

    elif class_name == "Organic":
        topText = "This is organic waste! It goes to the brown bin (Biomüll)"
        picture = get_picture(image_paths[class_name])
        extraText= ""

    return topText, picture, extraText
