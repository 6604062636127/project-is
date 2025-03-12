import streamlit as st
import pandas as pd
import joblib

# โหลดโมเดลที่เทรนไว้
model = joblib.load("Housing.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🏡 House Price Prediction App")
st.write("ใส่ข้อมูลเกี่ยวกับบ้านเพื่อทำนายราคา")

# สร้างอินพุตให้ผู้ใช้ป้อนข้อมูล
area = st.number_input("พื้นที่ (ตร.ฟุต)", min_value=500, max_value=20000, step=100)
bedrooms = st.number_input("จำนวนห้องนอน", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("จำนวนห้องน้ำ", min_value=1, max_value=5, step=1)
stories = st.number_input("จำนวนชั้น", min_value=1, max_value=4, step=1)
parking = st.number_input("ที่จอดรถ", min_value=0, max_value=5, step=1)

# ฟีเจอร์ที่แปลงจากข้อมูลเดิม
price_per_sqft = area / 1000  # ปรับการคำนวณให้เหมาะสมกับข้อมูลของคุณ
rooms_per_sqft = (bedrooms + bathrooms) / area
parking_per_sqft = parking / area

# สร้าง DataFrame จากข้อมูลที่ผู้ใช้ป้อน
X_new = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "parking": [parking],
    "price_per_sqft": [price_per_sqft],
    "rooms_per_sqft": [rooms_per_sqft],
    "parking_per_sqft": [parking_per_sqft]
})

# ตรวจสอบให้แน่ใจว่า X_new มีฟีเจอร์เหมือนกับข้อมูลที่ใช้ฝึกฝน
# (หากใช้ pandas DataFrame) คุณสามารถแปลงเป็น numpy array
X_new = X_new.values

# ปรับมาตรฐานข้อมูลใหม่ด้วย StandardScaler ที่ฝึกไว้
X_new_scaled = scaler.transform(X_new)

# ทำนายราคาบ้าน
if st.button("🔮 ทำนายราคา"):
    predicted_price = model.predict(X_new_scaled)
    st.success(f"🏠 ราคาบ้านที่ทำนายได้: {predicted_price[0]:,.2f} บาท")
