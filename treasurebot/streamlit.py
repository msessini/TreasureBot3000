

import streamlit as st
import requests
import json
from treasurebot.interface.main import generate_output

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

st.title("TreasureBot")
st.write("Welcome to treasurebot 🤖 I will help you to dispose your waste into the correct bins.")
st.caption("Upload an image and click 'Predict' to see in which bin it needs to go.")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg','jpeg','png'])
@st.dialog("waste")
def predictedbin(output):
    st.write(output[0])

    if bincolor == 'brown':
        st.image(output[1])
        st.write(output[2])
        
if uploaded_file is not None:
    st.image(uploaded_file)

    # Form to submit the prediction
    form_submitted = False

    with st.form("prediction_form"):
        submitted = st.form_submit_button("Predict")

        if submitted:
            form_submitted = True

            # api_url = "your_api_url_here"
            # files = {"file": uploaded_file}
            # result = requests.post(api_url, files=files).json()


            prediction = #should be the result of the api

            predictedbin(generate_output(prediction))

    if form_submitted:
        st.write("Prediction submitted!")



st.markdown('##')


st.write("please leave a review ⭐️ ")
st.feedback(options="stars", key=None, disabled=False, on_change=None, args=None, kwargs=None)
