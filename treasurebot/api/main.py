from fastapi import FastAPI, UploadFile, File
from PIL import Image
import numpy as np  # Import NumPy for array operations
from treasurebot.ml_logic.registry import get_model
from treasurebot.ml_logic.preprocessor import preprocess_image
from treasurebot.ml_logic.data import get_picture
import os


# Load environment variables

app = FastAPI()
app.state.model = get_model()
#image: UploadFile = File()

@app.get("/classify")
async def classify_image():
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # moving to the root directory
    parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
    # Construct the path to the 'test.jpg' file
    image_path = os.path.join(parent_dir, 'pictures', 'test.jpg')

    # Preprocess the image using the defined function
    #preprocessed_image = preprocess_image('/home/muhammad/code/Muhammad-Nou/TreasureBot3000/pictures/test.jpg')
    preprocessed_image = preprocess_image(image_path)
    # Make a prediction using your model (replace with your model call)
    prediction = app.state.model.predict(preprocessed_image)

    return {"prediction": str(prediction)}
print(classify_image())
#
@app.get('/')
def root():
    return {'Mohammed': 'trash_can'}
