import streamlit as st

try:
    from predict_page import show_predict_page
except ImportError:
    pass


show_predict_page()

