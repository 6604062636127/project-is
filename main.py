# app.py

import streamlit as st
import numpy as np
import pickle

# Load the saved model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the user interface
st.title("การทำนายราคาอสังหาริมทรัพย์")
st.write("กรุณากรอกข้อมูลฟีเจอร์เพื่อทำนายราคา:")

# Input features
area = st.number_input("พื้นที่ (ตารางฟุต)", min_value=0.0, value=0.0)
bathrooms = st.number_input("จำนวนห้องน้ำ", min_value=0, value=0)
bedrooms = st.number_input("จำนวนห้องนอน", min_value=0, value=0)
parking = st.number_input("จำนวนที่จอดรถ", min_value=0, value=0)

# Button to make prediction
if st.button("ทำนาย"):
    # Create feature array
    features = np.array([[area, bathrooms, bedrooms, parking]])
    
    # Check the number of features
    if features.shape[1] != model.n_features_in_:
        st.error(f"จำนวนฟีเจอร์ที่ป้อน ({features.shape[1]}) ไม่ตรงกับจำนวนฟีเจอร์ที่โมเดลคาดหวัง ({model.n_features_in_})")
    else:
        prediction = model.predict(features)
        st.write(f"ราคาที่คาดการณ์: {prediction[0]:.2f} บาท")

# Run the app
if __name__ == '__main__':
    st.write("แอปนี้ใช้โมเดล Random Forest เพื่อทำนายราคาอสังหาริมทรัพย์จากฟีเจอร์ที่ป้อน")
