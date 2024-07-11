import streamlit as st
import requests

# ngrok URL (replace with your actual ngrok URL)
NGROK_URL = "https://5a2f-2402-4000-20c1-fe90-15ed-4a89-8354-3e0.ngrok-free.app/move_servo"

# Function to move the servo to a random position
def move_servo():
    response = requests.post(NGROK_URL)
    if response.status_code == 200:
        data = response.json()
        st.write(data["message"])
    else:
        st.error("Failed to move servo")

# Streamlit app interface
st.title("Servo Motor Control")  # Title of the Streamlit app
if st.button("Move Servo"):  # Button to trigger servo movement
    move_servo()  # Call the function to move the servo
