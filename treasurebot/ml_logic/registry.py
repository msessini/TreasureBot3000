import os
from treasurebot.params import *
from tensorflow.keras.models import load_model


def get_model():
    #if MODEL_TARGET == 'local':
    model = load_model(os.path.join(LOCAL_MODELS_PATH, 'model.keras'))
    return model
