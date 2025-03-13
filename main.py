import streamlit as st
import pandas as pd
import pickle

# โหลดโมเดลที่ถูกฝึกไว้
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# ชื่อของแอปพลิเคชัน
st.title("House Price Prediction App")

# ส่วนสำหรับการป้อนข้อมูล
st.header("Input Features")

# ป้อนข้อมูลพื้นที่
area = st.number_input("Area (in square meters)", min_value=0.0)

# ป้อนข้อมูลฟีเจอร์อื่น ๆ ตามที่จำเป็น
# ตัวอย่างเช่น:
# num_bedrooms = st.number_input("Number of Bedrooms", min_value=0)
# num_bathrooms = st.number_input("Number of Bathrooms", min_value=0)

# สร้าง DataFrame สำหรับข้อมูลที่ป้อน
input_data = pd.DataFrame({
    'area': [area],
    # เพิ่มฟีเจอร์อื่น ๆ ที่คุณต้องการที่นี่
})

# ปุ่มสำหรับการทำนายราคา
if st.button("Predict Price"):
    predicted_price = model.predict(input_data)
    st.write(f"The predicted house price is: {predicted_price[0]:.2f} บาท")

# ข้อความแนะนำ
st.write("กรุณากรอกข้อมูลด้านบนและคลิก 'Predict Price' เพื่อดูราคาที่คาดการณ์ไว้.")
