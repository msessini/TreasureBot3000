from treasurebot.params import *


def get_picture(name):
    picture = os.path.join(LOCAL_PICTURES_PATH, name)
    return picture
