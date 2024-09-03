import numpy as np

classes = ['Aluminium', 'Closhoes', 'DrinkCans', 'Glass', 'GlassBottles', 'Organic', 'Paperboard', 'Piles', 'Plastic', 'PlasticBottles']

def get_label(prediction):
    print(prediction)
    return classes[np.argmax(prediction)]
