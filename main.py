import streamlit as st
import joblib
import pandas as pd

# โหลดโมเดลและ scaler ที่บันทึกไว้
model = joblib.load('house_price_model.pkl')
scaler = joblib.load('scaler.pkl')

# ชื่อแอปและคำอธิบาย
st.title("🏡 House Price Prediction App")
st.write("กรุณากรอกข้อมูลเกี่ยวกับบ้านเพื่อทำนายราคา")

# รับข้อมูลจากผู้ใช้
area = st.number_input("พื้นที่ (ตร.ฟุต)", min_value=500, max_value=20000, step=100)
bedrooms = st.number_input("จำนวนห้องนอน", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("จำนวนห้องน้ำ", min_value=1, max_value=5, step=1)
stories = st.number_input("จำนวนชั้น", min_value=1, max_value=4, step=1)
parking = st.number_input("ที่จอดรถ", min_value=0, max_value=5, step=1)

# คำนวณฟีเจอร์ที่แปลงจากข้อมูลเดิม
price_per_sqft = area / 1000
rooms_per_sqft = (bedrooms + bathrooms) / area
parking_per_sqft = parking / area

# สร้าง DataFrame สำหรับข้อมูลใหม่
X_new = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'stories': [stories],
    'parking': [parking],
    'price_per_sqft': [price_per_sqft],
    'rooms_per_sqft': [rooms_per_sqft],
    'parking_per_sqft': [parking_per_sqft]
})

# สเกลข้อมูลใหม่
X_new_scaled = scaler.transform(X_new)

# ทำนายราคา
if st.button("🔮 ทำนายราคา"):
    predicted_price = model.predict(X_new_scaled)
    st.success(f"🏠 ราคาบ้านที่ทำนายได้: {predicted_price[0]:,.2f} บาท")

