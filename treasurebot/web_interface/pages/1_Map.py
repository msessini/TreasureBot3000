import streamlit as st
from streamlit_folium import folium_static
from pathlib import Path
import base64
from map import make_map

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

# Apply background image
add_bg_from_local("bgv.png")

# Apply custom CSS styling
st.markdown("""
    <style>
     .css-16idsys p {
        color: white;
        margin: 0 auto;
        font-size: larger;
    }
    /* Centered title text styling */
    .centered-text {
        color: #E0E0E0;
        font-size: 46px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }

    .st-b3 {
        justify-content: center;
        color: white;
    }

    .st-b3 > div {
        color: white;
    }

    .css-6qob1r {
        background-color:black;
    }

    .css-pkbazv {
        color: white;
    }

    .css-18ni7ap {
        background-color:black;
    }

    .css-16idsys {
    font-family: "Source Sans Pro", sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    }

    /* Text input label and radio label styling */
    .stTextInput > div > label, .stRadio > div > label {
        color: #E0E0E0 !important;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
    }

    /* Text input field styling */
    .stTextInput > div > div > input {
        color: #E0E0E0;
        background-color: #333333;
        border-radius: 5px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        width: 100%;
    }

    /* Radio button container styling */
    .stRadio > div > div {
        color: #E0E0E0;
        display: flex;
        justify-content: center;
    }

    /* Radio button label styling */
    .stRadio > div > div > label {
        color: #E0E0E0 !important;
        font-size: 18px;
    }

    /* Center the map */
    .stFolium {
        display: flex;
        justify-content: center;
    }

    /* Center content within columns */
    [data-testid="column"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content-center;
    }

    /* Ensure radio button text is colored correctly */
    .stRadio label span {
        color: #E0E0E0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Centered section title
st.markdown('<div class="centered-text">Recycling map</div>', unsafe_allow_html=True)

# Create a centered form layout
st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
with st.container():
    st.markdown('<div style="width: 100%; max-width: 600px;">', unsafe_allow_html=True)

    # Centered input label and field
    address = st.text_input("Find the nearest recycling containers around you by entering your address:")

    # Centered radio label and options
    kind = st.radio(
        "What do you want to recycle?",
        options=["Glass", "Clothes", "Batteries", "Pfand return"],
        horizontal=True
    )

    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Display the map only if an address is provided
if address:
    fmap = make_map(address, kind)
    if not fmap:
        st.markdown('<div class="centered-text" style="font-size: 20px;">😱 Address not found, please try something else.</div>', unsafe_allow_html=True)
    else:
        folium_static(fmap)
