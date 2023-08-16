import streamlit as st
import pandas as pd
import numpy as np
import time
import requests


API_KEY = st.secrets["API_KEY"]
API_URL = "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


with st.form(key='my_form'):
    labels = st.multiselect('Choose your labels', ["apple", "carrot", "banana"])
    inputs = st.text_area('Enter your text for classification', 
	    "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!")
    payload = {
    "inputs": inputs,
    "parameters": {"candidate_labels": labels},
    }

    submitted = st.form_submit_button('Classify!')
    if submitted:
          output = query(payload)
          st.write(output)


