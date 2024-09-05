import streamlit as st
from streamlit_folium import folium_static
from pathlib import Path
import base64


# Function to add background image
def add_bg_from_local(image_file):
    image_path = Path(__file__).parent.parent / "bg_images" / image_file
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-position: center;
        }}
        </style>
    """, unsafe_allow_html=True)
add_bg_from_local("bgv.png")
# CSS styling
st.markdown("""
    <style>
    .centered-text {
        color: #E0E0E0;
        font-size: 32px;
        text-align: center;
        margin-bottom: 20px;
    }
    .centered-label {
        color: #E0E0E0;
        font-size: 20px;
        text-align: center;
        display: block;
        margin-bottom: 10px;
    }
    .centered-input {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .stTextInput > div > div > input {
        color: #E0E0E0;
        background-color: #333333;
        border-radius: 5px;
        padding: 10px;
        font-size: 18px;
        text-align: center;
        margin: auto;
        display: block;
        width: 100%;
        max-width: 400px;
    }
    .centered-radio-label {
        color: #E0E0E0;
        font-size: 20px;
        text-align: center;
        display: block;
        margin-bottom: 10px;
    }
    .centered-radio {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 20px;
    }
    .stRadio > div > div > label {
        color: #E0E0E0;
        font-size: 18px;
    }

    .css-6qob1r{
        background-color:black;
    }

    .css-18ni7ap{
        background-color:black;
    }

    .css-pkbazv{
        color:white;
    }
    </style>
""", unsafe_allow_html=True)

# Centered title
st.markdown('<div class="centered-text">About</div>', unsafe_allow_html=True)
# Centered input label and field
st.markdown(
    """
    <div style="color:white; font-size:18px; text-align: justify;">
        <p>Treasurebot 3000 is a project developed collaboratively at <a href="https://www.lewagon.com/berlin" style="color:lightblue;">Le Wagon Berlin</a> by Farah Khalifa,
        Muhammad Nouman, Belal Sajal, and Mario Sessini. This application utilizes a convolutional neural network for waste identification
        based on a pre-trained model called <a href="https://arxiv.org/abs/1512.03385" style="color:lightblue;">ResNet50</a> alongside a custom dense layer with 1024 neurons, followed by a prediction
        layer with 10 neurons corresponding to our 10 waste categories.</p>
        <p>Treasurebot 3000 can accurately identify and classify the following types of waste: glass bottles, paper/cardboard, aluminum cans, plastic, organic
        waste, glass, plastic bottles, clothes, aluminium, and batteries. When an image is uploaded, Treasurebot
        3000 analyzes it and provides a prediction, indicating the appropriate bin for waste disposal.</p>
        <p>For specific items like glass bottles, clothes, or batteries where the disposal bin is usually not available at home,
        users can enter their address into the search bar, and an integrated map will display the nearest recycling
        container locations for these items.</p>
    </div>
    """,
    unsafe_allow_html=True
)
