import streamlit as st
import numpy as np
import pickle

# โหลดโมเดลที่บันทึกไว้
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# สร้างส่วนติดต่อผู้ใช้
st.title("การทำนายราคาอสังหาริมทรัพย์")
st.write("กรุณากรอกข้อมูลฟีเจอร์เพื่อทำนายราคา:")

# ตัวอย่างฟีเจอร์ที่ผู้ใช้ต้องป้อน
area = st.number_input("พื้นที่ (ตารางฟุต)", min_value=0.0, value=0.0)
bedrooms = st.number_input("จำนวนห้องนอน", min_value=0, value=0)
bathrooms = st.number_input("จำนวนห้องน้ำ", min_value=0, value=0)
stories = st.number_input("จำนวนชั้น", min_value=0, value=0)
mainroad = st.selectbox("อยู่ใกล้ถนนหลักหรือไม่?", options=["ใช่", "ไม่ใช่"])
guestroom = st.number_input("จำนวนห้องแขก", min_value=0, value=0)
basement = st.selectbox("มีห้องใต้ดินหรือไม่?", options=["ใช่", "ไม่ใช่"])
hotwaterheating = st.selectbox("มีระบบทำความร้อนน้ำร้อนหรือไม่?", options=["ใช่", "ไม่ใช่"])
airconditioning = st.selectbox("มีเครื่องปรับอากาศหรือไม่?", options=["ใช่", "ไม่ใช่"])
parking = st.number_input("จำนวนที่จอดรถ", min_value=0, value=0)
prefarea = st.selectbox("อยู่ในพื้นที่ที่ต้องการหรือไม่?", options=["ใช่", "ไม่ใช่"])
furnishingstatus = st.selectbox("สถานะการตกแต่ง:", options=["ตกแต่งแล้ว", "ไม่ตกแต่ง", "ตกแต่งบางส่วน"])

# ปุ่มสำหรับทำนายผล
if st.button("ทำนาย"):
    # แปลงค่าที่ป้อนให้เป็นตัวเลข (0 หรือ 1) สำหรับฟีเจอร์ที่เป็นค่าทางเลือก
    mainroad = 1 if mainroad == "ใช่" else 0
    basement = 1 if basement == "ใช่" else 0
    hotwaterheating = 1 if hotwaterheating == "ใช่" else 0
    airconditioning = 1 if airconditioning == "ใช่" else 0
    prefarea = 1 if prefarea == "ใช่" else 0

    # แปลงสถานะการตกแต่งเป็นค่าตัวเลข (อาจต้องใช้การเข้ารหัสเพิ่มเติม)
    furnishingstatus_mapping = {"ตกแต่งแล้ว": 1, "ไม่ตกแต่ง": 0, "ตกแต่งบางส่วน": 0.5}
    furnishingstatus_encoded = furnishingstatus_mapping[furnishingstatus]

    # สร้างอาเรย์ฟีเจอร์
    features = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus_encoded]])
    
    # ทำนายราคา
    prediction = model.predict(features)
    st.write(f"ราคาที่คาดการณ์: {prediction[0]:.2f} บาท")

# รันแอป
if __name__ == '__main__':
    st.write("แอปนี้ใช้โมเดล Random Forest เพื่อทำนายราคาอสังหาริมทรัพย์จากฟีเจอร์ที่ป้อน")
