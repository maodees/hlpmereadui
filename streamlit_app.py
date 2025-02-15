import streamlit as st
import cv2
import easyocr
import numpy as np
from PIL import Image

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to process webcam input and extract text using EasyOCR
def extract_text_from_image(frame):
    # Convert the frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Use EasyOCR to extract text
    results = reader.readtext(frame_rgb)
    
    text = ""
    for result in results:
        text += result[1] + " "  # Extract the text part
    return text.strip()

# Function to start the webcam stream
def start_webcam_stream():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process the frame to extract text
        extracted_text = extract_text_from_image(frame)
        
        # Display the webcam feed in Streamlit
        st.image(frame, channels="BGR", caption="Webcam Feed", use_column_width=True)
        
        # Show extracted text if any
        if extracted_text:
            st.write(f"Extracted Text: {extracted_text}")
        
        # Stop the loop when 'Stop' button is clicked
        if st.button("Stop"):
            break

    cap.release()

# Streamlit app layout
st.title("Text Extraction from Webcam Feed")

st.write("""
    This app uses EasyOCR to extract text from the webcam feed.
    Click the button below to start scanning.
""")

# Button to start the webcam
if st.button("Start Scanning"):
    start_webcam_stream()

