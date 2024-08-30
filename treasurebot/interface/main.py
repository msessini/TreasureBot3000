from treasurebot.ml_logic.data import get_picture



def generate_output(class_name):


    if class_name == "DrinkCans":
        topText = "This is a drinking can! It goes to the yellow bin (Wertstofftonne)."
        picture = get_picture("bins/yellow_bin.png")
        extraText = "Remember to check if your can has a deposit before throwing it away."

    elif class_name == "GlassBottles":
        topText = "This is a glass bottle! It goes to the glass recycling bin (Glasiglus)."
        picture = get_picture("bins/glass_bin.png")
        extraText = "Remember to check if your bottle has a deposit before throwing it away."

    elif class_name == "PlasticBottles":
        topText = "This is a plastic bottle! It goes to the yellow bin (Wertstofftonne)."
        picture = get_picture("bins/yellow_bin.png")
        extraText = "Remember to check if your bottle has a deposit before throwing it away."

    elif class_name == "Aluminium":
        topText = "This is metal! It goes to the yellow bin (Wertstofftonne)."
        picture = get_picture("bins/glass_bin.png")
        extraText = ""

    elif class_name == "Glass":
        topText = "This is glass! It goes to the glass recycling bin (Glasiglus)."
        picture = get_picture("bins/glass_bin.png")
        extraText = ""

    elif class_name == "Plastic":
        topText = "This is plastic! It goes to the yellow bin (Wertstofftonne)."
        picture = get_picture("bins/yellow_bin.png")
        extraText = ""

    elif class_name == "Paper":
        topText = "This is paper! It goes to the blue bin (Altpaper)."
        picture = get_picture("bins/blue_bin.png")
        extraText = ""

    elif class_name == "Cardboard":
        topText = "This is cardboard! It goes to the blue bin (Altpaper)."
        picture = get_picture("bins/blue_bin.png")
        extraText = ""

    elif class_name == "Organic":
        topText = "This is organic waste! It goes to the brown bin (Biomüll)"
        picture = get_picture("bins/brown_bin.png")
        extraText= ""
    else:
        topText = ""
        picture = ""
        extraText = ""

    return (topText, picture, extraText)
