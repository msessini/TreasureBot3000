from treasurebot.ml_logic.data import get_picture



def generate_output(class_name):

    match class_name:
        case "DrinkCans":
            topText = "This is a drinking can! It goes to the yellow bin (Wertstofftonne)."
            picture = get_picture("bins/yellow_bin_.png")
            extraText = "Remember to check if your can has a deposit before throwing it away."

        case "GlassBottles":
            topText = "This is a glass bottle! It goes to the glass recycling bin (Glasiglus)."
            picture = get_picture("bins/glass_bin_.png")
            extraText = "Remember to check if your bottle has a deposit before throwing it away."

        case "PlasticBottles":
            topText = "This is a plastic bottle! It goes to the yellow bin (Wertstofftonne)."
            picture = get_picture("bins/yellow_bin_.png")
            extraText = "Remember to check if your bottle has a deposit before throwing it away."

        case "Aluminium":
            topText = "This is metal! It goes to the yellow bin (Wertstofftonne)."
            picture = get_picture("bins/glass_bin_.png")
            extraText = ""

        case "Glass":
            topText = "This is glass! It goes to the glass recycling bin (Glasiglus)."
            picture = get_picture("bins/glass_bin_.png")
            extraText = ""

        case "Plastic":
            topText = "This is plastic! It goes to the yellow bin (Wertstofftonne)."
            picture = get_picture("bins/yellow_bin_.png")
            extraText = ""

        case "Paper":
            topText = "This is paper! It goes to the blue bin (Altpaper)."
            picture = get_picture("bins/blue_bin_.png")
            extraText = ""

        case "Cardboard":
            topText = "This is cardboard! It goes to the blue bin (Altpaper)."
            picture = get_picture("bins/blue_bin_.png")
            extraText = ""

        case "Organic":
            topText = "This is organic waste! It goes to the brown bin (Biomüll)"
            picture = get_picture("bins/brown_bin_.png")
            extraText= ""

return (topText, picture, extraText)
