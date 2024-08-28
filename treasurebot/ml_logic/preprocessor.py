from tensorflow.image import resize 



def preprocess_image(image):
    image = image.resize((254, 254))  # Resize
    return image.reshape((-1, 254, 254, 3))  # Reshape for model input
