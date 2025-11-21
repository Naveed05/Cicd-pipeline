import streamlit as st
import numpy as np
import pandas as pd
import joblib

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="Iris Classifier", page_icon="🌸", layout="centered")

st.title("🌸 Iris Flower Classification App")
st.write("Enter the flower measurements below to predict the species.")

# ------------------------------
# LOAD TRAINED MODEL
# ------------------------------
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")   # Make sure model.pkl is in same folder

model = load_model()

# ------------------------------
# INPUT UI
# ------------------------------
st.header("📥 Enter Measurements")

sepal_length = st.number_input("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width  = st.number_input("Sepal Width (cm)", 2.0, 5.0, 3.5)
petal_length = st.number_input("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width  = st.number_input("Petal Width (cm)", 0.1, 3.0, 0.2)

# ----------------------------------------------------------
# Feature Engineering (same as training_model.py)
# ----------------------------------------------------------
sepal_ratio = sepal_length / sepal_width
petal_ratio = petal_length / petal_width

# Final input vector (same order as your training code)
input_features = np.array([[ 
    sepal_length,
    sepal_width,
    petal_length,
    petal_width,
    sepal_ratio,
    petal_ratio
]])

# ------------------------------
# Predict Button
# ------------------------------
if st.button("🔍 Predict Species"):
    prediction = model.predict(input_features)[0]
    species = ["Setosa", "Versicolor", "Virginica"]

    st.success(f"🌿 Predicted Species: **{species[int(prediction)]}**")

# Footer
st.write("---")
st.write("Made with ❤️ using Streamlit & scikit-learn")
