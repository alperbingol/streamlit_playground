import streamlit as st
#import sklearn
from predict_page import show_predict_page
import pandas as pd
import os

current_directory = pd.__file__


# Get the parent directory
parent_directory = os.path.dirname(current_directory)

# List all directories in the parent directory
directories_in_parent = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Print the list of directories
for directory in directories_in_parent:
    st.write(directory)

show_predict_page()

