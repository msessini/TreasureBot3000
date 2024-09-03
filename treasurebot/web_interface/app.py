import streamlit as st
from datetime import datetime, timedelta
from pathlib import Path
import requests
from PIL import Image
import base64
import time
import os
import sys
from io import BytesIO

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from treasurebot.interface.main import generate_output

# Get the directory of the current script
current_dir = os.path.dirname(__file__)
print(f"Current directory: {current_dir}")

# Construct the path to the image file
image_path = os.path.join(current_dir, "bg_images", "TB.gif")
print(f"Constructed image path: {image_path}")

# Check if the file exists
if os.path.exists(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <style>
        .centered-image {{
            display: flex;
            justify-content: center;
        }}
        </style>
        <div class="centered-image">
            <img src="data:image/png;base64,{encoded_string}" width="200">
        </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Image file not found at: {image_path}")
st.markdown("<p class='welcome-text'>Welcome to TreasureBot 🤖<br>I will help you to dispose your waste into the correct bins.</p>", unsafe_allow_html=True)#

def add_bg_from_local(image_file):
    image_path = Path(__file__).parent / "bg_images" / image_file
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{ background-image: url(data:image/png;base64,{encoded_string}); background-size: cover; }}
        </style>
    """, unsafe_allow_html=True)

add_bg_from_local("bgv.png")

# Custom CSS for styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');
    .center-image{ display: flex; justify-content: center; align-items: center; }
    .title { font-family: 'Roboto', 'Open Sans', sans-serif; font-size: 72px; font-weight: 900; color: #FFD700; text-align: center; padding: 20px 0;}
    .welcome-text, .caption { font-family: 'Streamlit Sans', sans-serif; font-weight: bold; color: #E0E0E0; text-align: center; margin: 0; }
    .welcome-text { font-size: 20px; line-height: 1.2; margin-top: 10px; }
    .caption { font-size: 16px; margin-top: 10px; margin-bottom: 20px; }
    .popup-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background-color:rgba(0,0,0,0.8);display:flex;justify-content:center;align-items:center;z-index:9999;}
    .popup-content{background-color:white;padding:20px;border-radius:10px;text-align:center;max-width:370px;width:100%;}
    .popup-text{font-size:18px;font-weight:bold;margin-bottom:15px;}
    .popup-extra{font-size:15px;font-weight:bold;margin-top:10px;color:#555;}
     button {background-color:#007bff;color:white;border:none;padding:10px 20px;border-radius:5px;cursor:pointer;}
    </style>
""", unsafe_allow_html=True)

# Caption right above the file uploader
st.markdown("""
    <style>
    .caption {
        margin-bottom: 5px;  /* Adjusts the space below the caption */
        font-size: 16px;     /* You can also adjust the font size if needed */
    }
    .stFileUploader {
        margin-top: 0px;  /* Reduces the space above the file uploader */
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='caption'>Upload an image and click 'Predict' to see in which bin it needs to go.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...")

def resize_image(image, size=(400, 400)):
    img = Image.open(image) if not isinstance(image, Image.Image) else image
    img.thumbnail(size)
    return img

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

if uploaded_file:
    resized_image = resize_image(uploaded_file)
    st.image(resized_image, caption="Uploaded Image", use_column_width=False, width=400)

    with st.form("prediction_form"):
        if st.form_submit_button("Predict"):
            api_url = "http://127.0.0.1:8000/uploadfile"
            uploaded_file.seek(0)
            files = {"image": ("image.jpg", uploaded_file, "image/jpeg")}
            response = requests.post(api_url, files=files)

            if response.status_code == 200:
                result = response.json()
                top_text, bin_image, extra_text = generate_output(result.get("prediction"))

                if isinstance(bin_image, Image.Image):
                    # Convert the bin_image to a base64 string
                    bin_image_base64 = image_to_base64(bin_image)

                    st.markdown(f"""
    <div class="popup-overlay">
        <div class="popup-content">
            <p class="popup-text">{top_text}</p>
            <img src="data:image/png;base64,{bin_image_base64}" width="400px">
            <p class="popup-extra">{extra_text}</p>
            <button id="closePopup">Close</button>
        </div>
    </div>
    <script>
    document.getElementById('closePopup').addEventListener('click', function() {{
        window.location.replace('/');  // Redirects to the home page
    }});
    </script>
""", unsafe_allow_html=True)

st.markdown('##')
st.markdown('##')
st.markdown('##')

# Feedback Section
st.markdown("""
    <div class="feedback-section">
        <h3>How would you rate your experience?</h3>
        <div class="stars">
""", unsafe_allow_html=True)

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")

st.markdown("""
        </div>
    </div>
""", unsafe_allow_html=True)

if selected is not None:
    st.markdown(f"<div class='feedback-section'><p>You selected {sentiment_mapping[selected]} star(s).</p></div>", unsafe_allow_html=True)

# Initialize session state variables
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False
    st.session_state.popup_end_time = None

# Add the "Let's Recycle" button
st.markdown("""
    <div class="feedback-section">
        <div class="lets-recycle-btn">
""", unsafe_allow_html=True)

if st.button("Let's Recycle"):
    if selected is not None:
        st.session_state.show_popup = True
        st.session_state.popup_end_time = datetime.now() + timedelta(seconds=3)
    else:
        st.warning("<div class='feedback-section warning'>Please select a rating before clicking 'Let's Recycle'.</div>", unsafe_allow_html=True)

# Display the popup if conditions are met
if st.session_state.show_popup:
    current_time = datetime.now()
    if st.session_state.popup_end_time and current_time < st.session_state.popup_end_time:
        st.markdown("""
            <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.7); display: flex; justify-content: center; align-items: center; z-index: 1000;">
                <div style="background-color: white; padding: 20px; border-radius: 10px; text-align: center; max-width: 80%;">
                    <p style="font-size: 24px; font-weight: bold;">Thank you for your feedback!</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.session_state.show_popup = False
