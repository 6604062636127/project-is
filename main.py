import streamlit as st
import pickle
import numpy as np

# โหลดโมเดลจากไฟล์ model.pkl
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# หัวข้อหลัก
st.title("ยินดีต้อนรับสู่แอป Streamlit ของฉัน!")

# ส่วนสำหรับรับข้อมูลจากผู้ใช้
st.header("กรอกข้อมูลเพื่อทำการพยากรณ์")
input_feature1 = st.number_input("คุณสมบัติ 1:", value=0.0)
input_feature2 = st.number_input("คุณสมบัติ 2:", value=0.0)
input_feature3 = st.number_input("คุณสมบัติ 3:", value=0.0)

# เมื่อผู้ใช้กดปุ่มพยากรณ์
if st.button("ทำการพยากรณ์"):
    # สร้างอาร์เรย์จากข้อมูลที่ผู้ใช้กรอก
    input_data = np.array([[input_feature1, input_feature2, input_feature3]])
    
    # ทำการพยากรณ์
    prediction = model.predict(input_data)
    
    # แสดงผลลัพธ์
    st.write(f"ผลลัพธ์การพยากรณ์: {prediction[0]}")

# ส่วนท้าย
st.write("ขอบคุณที่เข้าชมแอปของเรา!")
