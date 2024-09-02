import os
from treasurebot.params import *
from tensorflow.keras.models import load_model

def get_model():

    current_dir = os.path.dirname(__file__)
    model_path = os.path.abspath(os.path.join(current_dir, '..', 'models', 'model_v6.h5'))
    model = load_model(model_path)
    return model
