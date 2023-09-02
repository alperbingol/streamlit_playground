import streamlit as st
from predict_page import show_predict_page

import sys

print("Python Version:", sys.version)
st.write("Python Version:", sys.version)


show_predict_page()

