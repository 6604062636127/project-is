import streamlit as st
import pandas as pd
import numpy as np
import pickle
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)
st.title("Random Forest Price Prediction")
st.write("Enter the features to predict the price:")

# ตัวอย่างฟีเจอร์ที่ผู้ใช้ต้องป้อน
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")
feature4 = st.number_input("Feature 4")
if st.button("Predict"):
    features = np.array([[feature1, feature2, feature3, feature4]])
    prediction = model.predict(features)
    st.write(f"Predicted Price: {prediction[0]}")
