from treasurebot.params import *
from tensorflow.keras.preprocessing.image import load_img

def get_picture(name):

    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # moving to the root directory
    parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
    # Construct the path to the 'test.jpg' file
    image_path = os.path.join(parent_dir, 'pictures', name)
    # Load image
    picture = load_img(image_path, target_size = (254, 254))
    return picture
