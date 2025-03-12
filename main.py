import streamlit as st
import pandas as pd
import joblib

# โหลดโมเดลที่เทรนไว้
model = joblib.load("model.pkl")
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

# 🔹 ข้อมูลใหม่ (ต้องมีฟีเจอร์ครบถ้วน)
X_new = pd.DataFrame({
    'area': [5000],
    'bedrooms': [3],
    'bathrooms': [2],
    'stories': [2],
    'parking': [1],

})

# 🔹 คำนวณฟีเจอร์ที่สร้างไว้ตอน Train
X_new['price_per_sqft'] = 0  # ไม่รู้ราคาจริง ให้ใส่ค่า Placeholder
X_new['rooms_per_sqft'] = (X_new['bedrooms'] + X_new['bathrooms']) / X_new['area']
X_new['parking_per_sqft'] = X_new['parking'] / X_new['area']

# 🔹 แปลงข้อมูล Object ให้เป็นตัวเลข (ใช้ LabelEncoder ที่เคย Train ไว้)
for col in label_encoders:
    X_new[col] = label_encoders[col].transform(X_new[col])

# 🔹 จัดเรียงคอลัมน์ให้ตรงกับตอน Train
X_new = X_new[X_train.columns]

# 🔹 ทำนายราคาบ้าน
predicted_price = rf_model.predict(X_new)
print(f"ราคาบ้านที่ทำนายได้: {predicted_price[0]:,.2f} บาท")
