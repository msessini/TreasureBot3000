from tensorflow.image import resize
from tensorflow.keras.preprocessing.image import img_to_array

def preprocess_image(image):
    image = img_to_array(image)
    return image.reshape((-1, 254, 254, 3))  # Reshape for model input
