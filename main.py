import streamlit as st
import pandas as pd
import pickle

# โหลดโมเดล Random Forest
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# สร้าง UI สำหรับ Streamlit
st.title("การทำนายราคาอสังหาริมทรัพย์")
st.write("กรุณากรอกข้อมูลพื้นที่เพื่อทำนายราคา:")

# Input field for area
area = st.number_input("พื้นที่ (ตารางฟุต)", min_value=0, value=3000)

# Button to make prediction
if st.button("ทำนาย"):
    # เตรียมข้อมูลสำหรับการทำนาย
    input_data = pd.DataFrame({'area': [area]})
    
    # ตรวจสอบฟีเจอร์ที่โมเดลต้องการ
    model_features = model.feature_names_in_
    for feature in model_features:
        if feature not in input_data.columns:
            input_data[feature] = 0  # เพิ่มฟีเจอร์ที่ขาดหายไปด้วยค่า 0
    input_data = input_data[model_features]

    # ทำนายราคาบ้าน
    predicted_price = model.predict(input_data)

    # แสดงผลลัพธ์
    st.write(f"ราคาที่คาดการณ์: {predicted_price[0]:,.2f} บาท")
