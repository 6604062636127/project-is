# main.py
import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

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

# ฟีเจอร์ที่จำเป็นต้องใช้ในโมเดล (ไม่รวม price_per_sqft, rooms_per_sqft, parking_per_sqft)
X_new = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'stories': [stories],
    'parking': [parking],
    'mainroad': ['yes'],  # ต้องเพิ่มค่าหมวดหมู่ที่โมเดลฝึกไว้
    'guestroom': ['yes'],
    'basement': ['no'],
    'hotwaterheating': ['yes'],
    'airconditioning': ['no'],
    'prefarea': ['yes'],
    'furnishingstatus': ['furnished']
})

# แปลงฟีเจอร์ที่เป็นหมวดหมู่ด้วย LabelEncoder
le = LabelEncoder()
categorical_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                       'airconditioning', 'prefarea', 'furnishingstatus']

for col in categorical_columns:
    X_new[col] = le.fit_transform(X_new[col])

# สเกลข้อมูลใหม่ (ฟีเจอร์ที่ใช้ในการฝึกโมเดล)
X_new_scaled = scaler.transform(X_new)

# คำนวณฟีเจอร์ที่แปลงจากข้อมูลเดิมหลังจากการสเกลข้อมูล
price_per_sqft = area / 1000
rooms_per_sqft = (bedrooms + bathrooms) / area
parking_per_sqft = parking / area

# เพิ่มฟีเจอร์ใหม่ที่คำนวณ
X_new_scaled_with_new_features = pd.DataFrame(X_new_scaled, columns=[col for col in X_new.columns if col != 'price'])  # ให้ชื่อคอลัมน์เหมือนกับฟีเจอร์ที่ใช้ฝึก
X_new_scaled_with_new_features['price_per_sqft'] = price_per_sqft
X_new_scaled_with_new_features['rooms_per_sqft'] = rooms_per_sqft
X_new_scaled_with_new_features['parking_per_sqft'] = parking_per_sqft

# ทำนายราคา
if st.button("🔮 ทำนายราคา"):
    predicted_price = model.predict(X_new_scaled_with_new_features)
    st.success(f"🏠 ราคาบ้านที่ทำนายได้: {predicted_price[0]:,.2f} บาท")
