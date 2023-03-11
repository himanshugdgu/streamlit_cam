import tempfile
import streamlit as st
import cv2
import numpy as np

def main():
    st.set_page_config(page_title="Video")
    
    video = st.empty()
    while True:
        # Read frame from camera
        ret, frame = cap.read()

        # Check if frame is read
        if not ret:
            st.warning("Unable to read frame.")
            break

        # Convert frame to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display frame
        video.image(frame, channels="RGB")

    # Release camera
    cap.release()


global cap
cap = cv2.VideoCapture(2)

if __name__ == "__main__":

    main()
