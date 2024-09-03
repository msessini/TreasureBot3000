from tensorflow.image import resize
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input

def preprocess_image(image):

    image = img_to_array(image)
    image = preprocess_input(image) # Specific preprocess for ResNet50 rescaling pixels from -1 to 1
    return image.reshape((-1, 254, 254, 3))  # Reshape for model input
