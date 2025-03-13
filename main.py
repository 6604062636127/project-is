import streamlit as st
import pandas as pd
import numpy as np
import pickle

# โหลดโมเดล
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# สร้างฟังก์ชันสำหรับการทำนาย
def predict_price(area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus):
    # สร้าง DataFrame สำหรับฟีเจอร์
    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'stories': [stories],
        'mainroad': [mainroad],
        'guestroom': [guestroom],
        'basement': [basement],
        'hotwaterheating': [hotwaterheating],
        'airconditioning': [airconditioning],
        'parking': [parking],
        'prefarea': [prefarea],
        'furnishingstatus': [furnishingstatus]
    })

    # แปลงฟีเจอร์เชิงหมวดหมู่เป็นตัวเลข (One-Hot Encoding)
    input_data = pd.get_dummies(input_data, drop_first=True)

    # ตรวจสอบฟีเจอร์ที่โมเดลต้องการ
    model_features = model.feature_names_in_

    # เพิ่มฟีเจอร์ที่ขาดหายไปใน input_data
    for feature in model_features:
        if feature not in input_data.columns:
            input_data[feature] = 0  # เพิ่มฟีเจอร์ที่ขาดหายไปด้วยค่า 0

    # จัดเรียงฟีเจอร์ใน input_data ให้ตรงกับโมเดล
    input_data = input_data[model_features]

    # ทำการทำนาย
    prediction = model.predict(input_data)
    return prediction[0]

# สร้าง UI สำหรับ Streamlit
st.title("การทำนายราคาอสังหาริมทรัพย์")
st.write("กรุณากรอกข้อมูลฟีเจอร์เพื่อทำนายราคา:")

# Input fields
area = st.number_input("พื้นที่ (ตารางฟุต)", min_value=2000.0, value=0.0)
bedrooms = st.number_input("จำนวนห้องนอน", min_value=0, value=0)
bathrooms = st.number_input("จำนวนห้องน้ำ", min_value=0, value=0)
stories = st.number_input("จำนวนชั้น", min_value=0, value=0)
mainroad = st.selectbox("อยู่ใกล้ถนนหลักหรือไม่?", ["yes", "no"])
guestroom = st.selectbox("มีห้องแขกหรือไม่?", ["yes", "no"])
basement = st.selectbox("มีชั้นใต้ดินหรือไม่?", ["yes", "no"])
hotwaterheating = st.selectbox("มีระบบน้ำร้อนหรือไม่?", ["yes", "no"])
airconditioning = st.selectbox("มีเครื่องปรับอากาศหรือไม่?", ["yes", "no"])
parking = st.number_input("จำนวนที่จอดรถ", min_value=0, value=0)
prefarea = st.selectbox("อยู่ในพื้นที่ที่ต้องการหรือไม่?", ["yes", "no"])
furnishingstatus = st.selectbox("สถานะการตกแต่ง", ["furnished", "semi-furnished", "unfurnished"])

# Button to make prediction
if st.button("ทำนาย"):
    price_prediction = predict_price(area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus)
    st.write(f"ราคาที่คาดการณ์: {price_prediction:.2f} บาท")
