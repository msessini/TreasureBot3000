import os
from treasurebot.params import *


def load_model():
    #if MODEL_TARGET == 'local':
    model = os.path.join(LOCAL_MODELS_PATH, 'model.h5')
    return model
