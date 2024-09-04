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
image_path = os.path.join(current_dir, "bg_images", "GIF.gif")
print(f"Constructed image path: {image_path}")

# Check if the file exists
if os.path.exists(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <style>
        .css-6qob1r{{
                 background-color:black;}}
        .centered-image {{
            display: flex;
            justify-content: center;
        }}

        .css-18ni7ap{{
            visibility: hidden;
        }}
        .css-pkbazv{{
            color: white;
        }}

        </style>
        <div class="centered-image">
            <img src="data:image/png;base64,{encoded_string}" width="330">
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
    .center-image {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .title { font-family: 'Roboto', 'Open Sans', sans-serif; font-size: 72px; font-weight: 900; color: #FFD700; text-align: center; padding: 20px 0;}
    .welcome-text, .caption { font-family: 'Streamlit Sans', sans-serif; font-weight: bold; color: #E0E0E0; text-align: center; margin: 0; }
    .welcome-text { font-size: 20px; line-height: 1.2; }
    .caption { font-size: 16px; margin-top: 5px; margin-bottom: 5px; }
    .popup-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background-color:rgba(0,0,0,0.8);display:flex;justify-content:center;align-items:center;z-index:9999;}
    .popup-content{background-color:white;padding:10px;border-radius:10px;text-align:center;max-width:420px;width:90%;}
    .popup-text{font-size:18px;font-weight:bold;margin-bottom:15px;}
    .popup-extra{font-size:15px;font-weight:bold;margin-top:10px;color:#555;}
    button{background-color:#007bff;color:white;border:none;padding:10px 15px;border-radius:4px;cursor:pointer;}
    </style>
""", unsafe_allow_html=True)

# Title and welcome message
st.markdown("<p class='caption'>Upload an image and click 'Predict' to see in which bin it needs to go.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("")

def resize_image(image, size=(300,350)):
    img = Image.open(image) if not isinstance(image, Image.Image) else image
    img.thumbnail(size)
    return img

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

if uploaded_file:
    resized_image = resize_image(uploaded_file)

    # Custom CSS to center the image
    st.markdown("""
        <style>
        .centered-image {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .css-1v0mbdj img {
            width: 300px;
        }

        .uploadedFile {
            display: none;
        }

        .css-1v0mbdj {
            display: flex;
            justify-content: center;
            width: 100vw;
            flex-direction: row;
        }
        </style>
    """, unsafe_allow_html=True)

     # Display the image inside a centered div
    st.markdown("<div class='centered-image'>", unsafe_allow_html=True)
    st.image(resized_image, use_column_width=False, width=290)
    st.markdown("</div>", unsafe_allow_html=True)

    with st.form("prediction_form"):
        if st.form_submit_button("Predict"):
            api_url = "https://treasurebot3000-564754607351.europe-west1.run.app/uploadfile"
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
                                <img src="data:image/png;base64,{bin_image_base64}" width="330px">
                                <p class="popup-extra">{extra_text}</p>
                                <button id="closePopup">Close</button>
                            </div>
                        </div>
                        <script>
                        document.getElementById('closePopup').addEventListener('click', function() {{
                            document.querySelector('.popup-overlay').style.display = 'none';
                        }});
                        </script>
                    """, unsafe_allow_html=True)
                else:
                    st.error("No image found to display.")
            else:
                st.error(f'Error with code {response.status_code}, {response.content}')

st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')

# Custom CSS for styling
st.markdown("""
    <style>
    .rating-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-top: 20px;
    }
    .rating-header {
        color: #E0E0E0;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
    }
    .stRadio > div {
        display: flex;
        justify-content: center;
    }
    .stButton button {
        display: block;
        margin: 0 auto;
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 4px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Centered rating section
st.markdown("<div class='rating-section'>", unsafe_allow_html=True)
st.markdown("<div class='rating-header'>How would you rate your experience?</div>", unsafe_allow_html=True)

# Radio button for rating
rating = st.radio("", ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], horizontal=True)

# Button for submission
if st.button("Submit"):
    if rating:
        st.session_state.show_popup = True
        st.session_state.popup_end_time = datetime.now() + timedelta(seconds=3)
    else:
        st.warning("Please select a rating before clicking 'Let's Recycle'.")

st.markdown("</div>", unsafe_allow_html=True)

if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False
    st.session_state.popup_end_time = None

if st.session_state.show_popup and (st.session_state.popup_end_time - datetime.now()).total_seconds() > 0:
    st.markdown("""
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.7); display: flex; justify-content: center; align-items: center;">
            <div style="background-color: white; padding: 20px; border-radius: 10px; text-align: center; max-width: 80%;">
                <p style="font-size: 24px; font-weight: bold;">Thank you for your feedback!</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(0.1)
    st.experimental_rerun()
else:
    st.session_state.show_popup = False
