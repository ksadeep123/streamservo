import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# New ngrok URL
NGROK_URL = "https://93d5-123-231-111-80.ngrok-free.app/move_servos"

# Function to move the servos to random positions and capture an image
def move_servos():
    response = requests.post(NGROK_URL)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="Captured Image", use_column_width=True)
    else:
        st.error("Failed to move servos or capture image")

# Streamlit app interface
st.title("Servo Motor Control")  # Title of the Streamlit app
if st.button("Take a pic"):  # Button to trigger servo movement
    move_servos()  # Call the function to move the servos and capture image
