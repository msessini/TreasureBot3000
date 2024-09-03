import numpy as np

classes = ['Aluminium', 'DrinkCans', 'Glass', 'GlassBottles', 'Organic', 'Paperboard', 'Plastic', 'PlasticBottles']

def get_label(prediction):
    print(prediction)
    return classes[np.argmax(prediction)]
