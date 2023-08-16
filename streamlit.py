import streamlit as st
import pandas as pd
import numpy as np
import time
import requests
from datetime import datetime as dt

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False


API_KEY = st.secrets["API_KEY"]
API_URL = "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

if "mytsks" not in st.session_state:
    st.session_state.mytsks = []

tsk = st.text_input('Enter as many labels as you want:', value="", placeholder='Enter a label', key='task_input')
if st.button('Add Label'):
    if tsk != "":
        st.session_state.mytsks.append(tsk)
        #tsk = ""  # Reset the input box after adding a task


with st.form(key='my_form'):
    #labels = st.multiselect('Choose your labels', ["apple", "carrot", "banana"])
    labels = st.multiselect('Choose your labels', st.session_state.mytsks)
    inputs = st.text_area('Enter your text for classification:', 
	    "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!")
    payload = {
    "inputs": inputs,
    "parameters": {"candidate_labels": labels},
    }

    submitted = st.form_submit_button('Classify!')
    if submitted:
          output = query(payload)
          st.write(output)


#for task in st.session_state.mytsks:
    #st.write(task)


