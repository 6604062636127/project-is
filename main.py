import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# โหลดโมเดลที่ถูกฝึกไว้
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# ชื่อของแอปพลิเคชัน
st.title("House Price Prediction App")

# ส่วนสำหรับการป้อนข้อมูล
st.header("Input Feature")

# ป้อนข้อมูลพื้นที่บ้าน
area = st.number_input("Area of the house (in square meters)", min_value=0.0)

# สร้าง DataFrame สำหรับข้อมูลที่ป้อน
input_data = pd.DataFrame({
    'area': [area]
})

# ตรวจสอบให้แน่ใจว่า DataFrame มีฟีเจอร์ทั้งหมดที่โมเดลต้องการ
model_columns = model.feature_names_in_
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# ปุ่มสำหรับการทำนายราคา
if st.button("Predict Price"):
    predicted_price = model.predict(input_data)
    st.write(f"The predicted house price is: {predicted_price[0]:.2f} บาท")

    # แสดงกราฟ
    st.subheader("Price Prediction Visualization")
    
    # สร้างกราฟ
    plt.figure(figsize=(10, 5))
    plt.bar(['Predicted Price'], [predicted_price[0]], color='blue')
    plt.ylabel('Price (Baht)')
    plt.title('Predicted House Price Based on Area')
    plt.ylim(0, predicted_price[0] * 1.2)  # ขยายขอบเขต Y-axis
    plt.grid(axis='y')

    # แสดงกราฟใน Streamlit
    st.pyplot(plt)

# ข้อความแนะนำ
st.write("กรุณากรอกข้อมูลด้านบนและคลิก 'Predict Price' เพื่อดูราคาที่คาดการณ์ไว้.")
