from tensorflow.image import resize
from tensorflow.keras.preprocessing.image import img_to_array, load_img

def preprocess_image(image):

    image = load_img(image, target_size=(254,254))
    image = img_to_array(image)
    return image.reshape((-1, 254, 254, 3))  # Reshape for model input
