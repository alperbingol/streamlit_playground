import streamlit as st
import pandas as pd
import pickle
import numpy as np
#import sklearn
import subprocess
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Display the Streamlit version
st.write(f"Streamlit Version: {st.__version__}")
#st.write(f"Sklearn Version: {sklearn.__version__}")


def load_model():
    with open('saved_steps2.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]


def show_predict_page():
    st.title("Software Developer Salary Predition")
    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )
   
    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )
    
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)
    
    expericence = st.slider("Years of Experience", 0, 50, 3)
    
    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)
        
        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")