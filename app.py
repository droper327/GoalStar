# Import streamlit and other libraries
import streamlit as st
import streamlit_webrtc as webrtc
import streamlit_aggrid as st_aggrid
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import firebase_admin
from firebase_admin import credentials, storage, db
import av

# Set the page title and configuration
st.set_page_config(page_title="Goal Action App", page_icon="🎯", layout="wide")

# Create the title and subtitle of the app
st.title("Goal Action App")
st.subheader("A streamlit app that helps you achieve your goals and track your progress")

# Create the sidebar and the navigation menu
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Create the session state to store the user's input and output
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "user_output" not in st.session_state:
    st.session_state.user_output = ""

# Define the video processor class
class VideoProcessor(webrtc.VideoProcessorBase):
    def __init__(self):
        self.videos = [] # A list to store the recorded videos

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24") # Convert the frame to a numpy array
        img = np.rot90(img, k=1) # Rotate the image by 90 degrees
        self.videos.append(img) # Append the image to the list
        return av.VideoFrame.from_ndarray(img, format="bgr24") # Return the processed frame

# Create a webrtc context
webrtc_ctx = webrtc.StreamlitWebrtc(
    key="video",
    mode=webrtc.WebRtcMode.SENDRECV,
    video_processor_factory=VideoProcessor,
    video_constraints={"width": 640, "height": 480, "frameRate": 30},
)

# Create a button to stop recording
if st.button("Stop recording"):
    webrtc_ctx.stop()

# Create a grid to display the recorded videos
if len(webrtc_ctx.video_processor.videos) > 0:
    grid_data = [{"video": f"<img src='{webrtc.image_to_url(video)}' />"} for video in webrtc_ctx.video_processor.videos]
    grid_options = {"columnDefs": [{"field": "video", "cellRenderer": "html"}]}
    st_aggrid.AgGrid(grid_data, gridOptions=grid_options, fit_columns_on_grid_load=True)
