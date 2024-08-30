import streamlit as st
import requests
from treasurebot.interface.main import generate_output
from treasurebot.ml_logic.data import get_picture
import base64
import sys
import os
from PIL import Image
import io

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Set page layout to wide
st.set_page_config(layout="wide")

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');

    .title {
        font-family: "Streamlit Sans Narrow', sans-serif;
        font-size: 50px;
        font-weight: bold;
        color: #ef6c00;
        text-align: center;
        padding: 20px 0;
        text-shadow: 2px 2px 4px #000000;
    }

    .welcome-text {
        font-size: 24px;
        color: #695d56;
        text-align: center;
        padding: 0;
        margin: 0;
        line-height: 1.2;
        text-shadow: 1px 1px 2px #000000;
    }

    .caption {
        font-size: 18px;
        color: #695d56;
        text-align: center;
        padding: 5px 0;
        text-shadow: 1px 1px 2px #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>TreasureBot 3000</h1>", unsafe_allow_html=True)

# Welcome message (combined into one paragraph)
st.markdown("<p class='welcome-text'>Welcome to TreasureBot 🤖<br>I will help you to dispose your waste into the correct bins.</p>", unsafe_allow_html=True)

# Caption
st.markdown("<p class='caption'>Upload an image and click 'Predict' to see in which bin it needs to go.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...")

def resize_image(image, size=(350, 350)):
    if isinstance(image, Image.Image):
        # If it's already a PIL Image object
        image.thumbnail(size)
        return image
    else:
        # If it's a file-like object (e.g., UploadedFile)
        img = Image.open(image)
        img.thumbnail(size)
        return img

if uploaded_file is not None:
    resized_image = resize_image(uploaded_file)
    st.image(resized_image, caption="Uploaded Image", use_column_width=False, width=350)

    # Form to submit the prediction
    with st.form("prediction_form"):
        submitted = st.form_submit_button("Predict")
        if submitted:
            # Call your API here
            api_url = "http://127.0.0.1:8000/uploadfile"

            # Reset file pointer to the beginning
            uploaded_file.seek(0)

            files = {"image": ("image.jpg", uploaded_file, "image/jpeg")}
            headers = {"accept": "application/json"}

            response = requests.post(api_url, files=files, headers=headers)

            if response.status_code == 200:
                result = response.json()
                prediction = result.get("prediction")  # Adjust this based on your API response structure

                # Generate output based on the prediction
                top_text, bin_image, extra_text = generate_output(prediction)

                # Display the results
                st.write(top_text)
                if bin_image:
                    resized_bin_image = resize_image(bin_image)
                    st.image(resized_bin_image, caption="Appropriate Bin", use_column_width=False, width=800)
                if extra_text:
                    st.write(extra_text)
            else:
                st.error(f'Error with code {response.status_code}, {response.content}')

# Rating section
st.markdown('##')
st.markdown('##')
st.markdown('##')

rating = st.radio(
    "How would you rate your experience?",
    ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
    horizontal=True
)

if rating:
    st.write(f"Thank you for your {rating} rating!")
