import streamlit as st
import numpy as np
import pickle

# โหลดโมเดลที่บันทึกไว้
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# สร้างส่วนติดต่อผู้ใช้
st.title("การทำนายราคาบ้าน")
st.write("กรุณากรอกข้อมูลฟีเจอร์เพื่อทำนายราคา:")

# ตัวอย่างฟีเจอร์ที่ผู้ใช้ต้องป้อน
area = st.number_input("พื้นที่ (ตารางฟุต)", min_value=0.0, value=0.0)
bathrooms = st.number_input("จำนวนห้องน้ำ", min_value=0, value=0)
bedrooms = st.number_input("จำนวนห้องนอน", min_value=0, value=0)
parking = st.number_input("จำนวนที่จอดรถ", min_value=0, value=0)

# ปุ่มสำหรับทำนายผล
if st.button("ทำนาย"):
    features = np.array([[area, bathrooms, bedrooms, parking]])
    prediction = model.predict(features)
    st.write(f"ราคาที่คาดการณ์: {prediction[0]:.2f} บาท")

# รันแอป
if __name__ == '__main__':
    st.write("แอปนี้ใช้โมเดล Random Forest เพื่อทำนายราคาอสังหาริมทรัพย์จากฟีเจอร์ที่ป้อน")
