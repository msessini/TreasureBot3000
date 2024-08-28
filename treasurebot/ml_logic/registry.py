import os
from treasurebot.params import *
from tensorflow.keras.models import load_model

def get_model():
    #if MODEL_TARGET == 'local':
    current_dir = os.path.dirname(__file__)
    model_path = os.path.abspath(os.path.join(current_dir, '..', 'models', 'model.keras'))
    model = load_model(model_path)
    return model
