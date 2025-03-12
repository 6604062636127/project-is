import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# โหลดโมเดลและ scaler
try:
    model = joblib.load('house_price_model.pkl')
    scaler = joblib.load('scaler.pkl')
    le = joblib.load('label_encoder.pkl')  # โหลด LabelEncoder ที่ฝึกไว้
except Exception as e:
    st.error(f"เกิดข้อผิดพลาดในการโหลดโมเดลหรือ scaler: {e}")

# ชื่อแอปและคำอธิบาย
st.title("🏡 แอปทำนายราคาบ้าน")
st.write("กรุณากรอกข้อมูลเกี่ยวกับบ้านเพื่อทำนายราคา")

# รับข้อมูลจากผู้ใช้
area = st.number_input("พื้นที่ (ตร.ฟุต)", min_value=500, max_value=20000, step=100)
bedrooms = st.number_input("จำนวนห้องนอน", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("จำนวนห้องน้ำ", min_value=1, max_value=5, step=1)
stories = st.number_input("จำนวนชั้น", min_value=1, max_value=4, step=1)
parking = st.number_input("ที่จอดรถ", min_value=0, max_value=5, step=1)

# เตรียมฟีเจอร์สำหรับการทำนาย
X_new = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'stories': [stories],
    'parking': [parking],
    'mainroad': ['yes'],  # ค่าตัวอย่าง
    'guestroom': ['yes'],
    'basement': ['no'],
    'hotwaterheating': ['yes'],
    'airconditioning': ['no'],
    'prefarea': ['yes'],
    'furnishingstatus': ['furnished']
})

# แปลงฟีเจอร์ที่เป็นหมวดหมู่ด้วย LabelEncoder ที่ฝึกไว้
for col in ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 
            'airconditioning', 'prefarea', 'furnishingstatus']:
    X_new[col] = le.transform(X_new[col])

# ตรวจสอบให้แน่ใจว่าคอลัมน์ตรงกับชุดข้อมูลที่ใช้ฝึก
expected_columns = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking', 
                    'mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                    'airconditioning', 'prefarea', 'furnishingstatus']

# แสดงผลการดีบัก
st.write("คอลัมน์ใน DataFrame ที่ป้อน:", X_new.columns.tolist())
st.write("คอลัมน์ที่คาดหวัง:", expected_columns)

# ตรวจสอบว่าคอลัมน์ตรงกันหรือไม่
if list(X_new.columns) != expected_columns:
    st.error("คอลัมน์ไม่ตรงกับข้อมูลที่คาดหวังสำหรับ scaler.")
