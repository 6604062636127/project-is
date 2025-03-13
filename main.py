import streamlit as st
import pandas as pd
import pickle

# โหลดโมเดล Random Forest
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# สร้าง UI สำหรับ Streamlit
st.title("การทำนายราคาบ้าน")
st.write("กรุณากรอกข้อมูลพื้นที่ (ตารางเมตร) เพื่อทำนายราคา:")

# Input field for area in square meters
area_m2 = st.number_input("พื้นที่ (ตารางเมตร)", min_value=0.0, value=30.0)

# Button to make prediction
if st.button("ทำนาย"):
    # แปลงพื้นที่เป็น DataFrame
    input_data = pd.DataFrame({'area': [area_m2]})

    # ทำนายราคาบ้าน
    predicted_price = model.predict(input_data)

    # แสดงผลลัพธ์
    st.write(f"ราคาที่คาดการณ์: {predicted_price[0]:,.2f} บาท")
