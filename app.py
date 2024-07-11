import streamlit as st
import serial
import random
import time

# Function to establish serial connection
def get_serial_connection(port, baud_rate):
    try:
        ser = serial.Serial(port, baud_rate)
        time.sleep(2)  # Wait for the connection to initialize
        return ser
    except serial.SerialException as e:
        st.error(f"SerialException: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
    return None

# Set up the serial connection
arduino = get_serial_connection('COM5', 9600)

# Function to move the servo to a random position
def move_servo():
    if arduino:
        position = random.randint(0, 180)  # Generate a random position between 0 and 180 degrees
        arduino.write(f"{position}\n".encode())  # Send the position to the Arduino
        st.write(f"Servo moved to position: {position}")
    else:
        st.error("Failed to establish serial connection")

# Streamlit app interface
st.title("Servo Motor Control")  # Title of the Streamlit app
if st.button("Move Servo"):  # Button to trigger servo movement
    move_servo()  # Call the function to move the servo

if arduino:
    arduino.close()  # Close the serial connection when done
