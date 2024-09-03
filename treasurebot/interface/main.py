from PIL import Image
from treasurebot.ml_logic.data import get_picture

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
        topText = "This is a drinking can! It goes to the yellow bin (Wertstoff)."
        picture = get_picture(image_paths[class_name])
        extraText = "Remember to check if your can has a pfand label before throwing it away."

    elif class_name == "GlassBottles":
        topText = "This is a glass bottle! It goes to the glass recycling bin (Glasstonne)."
        picture = get_picture(image_paths[class_name])
        extraText = "Remember to check if your bottle has a pfand label before throwing it away."

    elif class_name == "PlasticBottles":
        topText = "This is a plastic bottle! It goes to the yellow bin (Wertstoff)."
        picture = get_picture(image_paths[class_name])
        extraText = "Remember to check if your bottle has a pfand label before throwing it away."

    elif class_name == "Aluminium":
        topText = "This is metal! It goes to the yellow bin (Wertstoff)."
        picture = get_picture(image_paths[class_name])
        extraText = ""

    elif class_name == "Glass":
        topText = "This is glass! It goes to the glass recycling bin (Glasstonne)."
        picture = get_picture(image_paths[class_name])
        extraText = ""

    elif class_name == "Plastic":
        topText = "This is plastic! It goes to the yellow bin (Wertstoff)."
        picture = get_picture(image_paths[class_name])
        extraText = ""

    elif class_name == "Paperboard":
        topText = "This is paper/card! It goes to the blue bin (Altpapier)."
        picture = get_picture(image_paths[class_name])
        extraText = ""

    elif class_name == "Organic":
        topText = "This is organic waste! It goes to the brown bin (Bioabfall)"
        picture = get_picture(image_paths[class_name])
        extraText= ""

    return topText, picture, extraText
