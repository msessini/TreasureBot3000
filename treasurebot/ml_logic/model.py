import numpy as np 

classes = ['Aluminium', 'Cardboard', 'DrinkCans', 'Glass', 'GlassBottles', 'Organic', 'Paper', 'Plastic', 'PlasticBottles']

def get_label(prediction):

    return classes[np.argmax(prediction)]

    
