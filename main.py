import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
import joblib

# 1. โหลดโมเดลที่ฝึกไว้
model = joblib.load('house_price_model.pkl')

# 2. สร้างฟังก์ชันสำหรับการทำนายราคา
def predict_price(area, bedrooms, bathrooms, stories, parking):
    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'stories': [stories],
        'parking': [parking]
    })
    predicted_price = model.predict(input_data)
    return predicted_price[0]

# 3. สร้าง UI ด้วย Streamlit
st.title("House Price Prediction")
st.header("Enter the details of the house")

# 4. รับข้อมูลจากผู้ใช้
area = st.number_input("Area (in square feet)", min_value=0)
bedrooms = st.number_input("Number of Bedrooms", min_value=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1)
stories = st.number_input("Number of Stories", min_value=1)
parking = st.number_input("Number of Parking Spaces", min_value=0)

# 5. ปุ่มสำหรับทำนายราคา
if st.button("Predict Price"):
    price = predict_price(area, bedrooms, bathrooms, stories, parking)
    st.success(f"The predicted price of the house is: ${price:,.2f}")
