from fastapi import FastAPI, UploadFile, File
from PIL import Image
from treasurebot.ml_logic.registry import get_model
from treasurebot.ml_logic.preprocessor import preprocess_image
from treasurebot.ml_logic.data import get_picture
from treasurebot.ml_logic.model import get_label
import io


# Load environment variables
app = FastAPI()
app.state.model = get_model()
#image: UploadFile = File()

@app.get("/classify")
async def classify_image():

    image = get_picture('test.jpg')
    # Preprocess the image using the defined function
    preprocessed_image = preprocess_image(image)
    # Making prediction
    prediction = app.state.model.predict(preprocessed_image)
    # Get class label
    label = get_label(prediction)
    return {"prediction": str(label)}

@app.post("/uploadfile") # you need a post request when you want to send anything to the server (an image in this case)
async def create_upload_file(image: UploadFile=File(...)): # async funcs allow processes to run in parallel, in this case you will be able to have the API endpoint available while waiting for the user to upload the image. As long as the image is not processed the following code won't be executed, thanks to the await keyword

    # Load and resize picture
    contents = await image.read()
    image_pil = Image.open(io.BytesIO(contents))
    image_resized = image_pil.resize((254, 254))
    # Preprocess
    preprocessed_image = preprocess_image(image_resized)
    # Predict
    prediction = app.state.model.predict(preprocessed_image)
    # Get class label
    label = get_label(prediction)

    return {"prediction": label}


@app.get('/')
def root():
    return {'': 'trash_can'}
