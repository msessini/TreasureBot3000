import streamlit as st
import requests
from treasurebot.interface.main import generate_output
from treasurebot.ml_logic.data import get_picture


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Add this new section for custom CSS
st.markdown("""
<style>
.stApp {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Your existing background function
def add_bg_from_local():
     st.markdown(
    """
    <style>
    .stApp {
        background: url("./TreasureBot3000/treasurebot/streamlit/rob.jpg");
        background-size: cover;
        background-color: rgb(40 54 80):
    }
    </style>
    """,
    unsafe_allow_html=True
)

add_bg_from_local()

st.title("TreasureBot 3000")
st.write("Welcome to treasurebot :robot_face: I will help you to dispose your waste into the correct bins.")
st.caption("Upload an image and click 'Predict' to see in which bin it needs to go.")

uploaded_file = st.file_uploader("Choose an image...")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Form to submit the prediction
    with st.form("prediction_form"):
        submitted = st.form_submit_button("Predict")
        if submitted:
            # Call your API here
            api_url="http://127.0.0.1:8000/uploadfile"
            files ={"image": uploaded_file}
            headers ={"accept":"application/json"}

            response = requests.post(api_url, files=files, headers=headers)

            if response.status_code == 200:
                result = response.json()
                prediction = result.get("prediction")  # Adjust this based on your API response structure

                # Generate output based on the prediction
                top_text, bin_image, extra_text = generate_output(prediction)

                # Display the results
                st.write(top_text)
                st.image(bin_image, caption="Appropriate Bin", use_column_width=True)
                if extra_text:
                    st.write(extra_text)
            else:
                st.error(f'error with code {response.status_code}, {response.content}')

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
