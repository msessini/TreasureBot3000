from fastapi import FastAPI, UploadFile, File
from PIL import Image
import numpy as np  # Import NumPy for array operations
from treasurebot.ml_logic.registry import get_model
from treasurebot.ml_logic.preprocessor import preprocess_image
from treasurebot.ml_logic.data import get_picture

# Load environment variables

app = FastAPI()
app.state.model = get_model()
#image: UploadFile = File()

@app.get("/classify")
async def classify_image():
    # Open the image from the upload
    image = get_picture('test.jpg')

    # Preprocess the image using the defined function
    preprocessed_image = preprocess_image(image)

    # Make a prediction using your model (replace with your model call)
    prediction = app.state.model.predict(preprocessed_image)

    return {"prediction": prediction}
#
@app.get('/')
def root():
    return {'Mohammed': 'trash_can'}
