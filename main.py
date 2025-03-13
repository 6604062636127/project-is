import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# โหลดโมเดลจากไฟล์
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# สร้าง UI สำหรับ Streamlit
st.title("การทำนายราคาอสังหาริมทรัพย์")
st.write("กรุณากรอกข้อมูลด้านล่าง:")

# Input fields
area = st.number_input("พื้นที่ (ตารางเมตร)", min_value=0.0, value=100.0)
bedrooms = st.number_input("จำนวนห้องนอน", min_value=0, value=3)
bathrooms = st.number_input("จำนวนห้องน้ำ", min_value=0, value=2)
stories = st.number_input("จำนวนชั้น", min_value=1, value=1)
mainroad = st.selectbox("อยู่ใกล้ถนนหลักหรือไม่", ['yes', 'no'])
guestroom = st.selectbox("มีห้องแขกหรือไม่", ['yes', 'no'])
basement = st.selectbox("มีชั้นใต้ดินหรือไม่", ['yes', 'no'])
hotwaterheating = st.selectbox("มีระบบน้ำร้อนหรือไม่", ['yes', 'no'])
airconditioning = st.selectbox("มีเครื่องปรับอากาศหรือไม่", ['yes', 'no'])
parking = st.number_input("จำนวนที่จอดรถ", min_value=0, value=1)
prefarea = st.selectbox("อยู่ในพื้นที่ที่ต้องการหรือไม่", ['yes', 'no'])
furnishingstatus = st.selectbox("สถานะการตกแต่ง", ['furnished', 'semi-furnished', 'unfurnished'])

# Button to make prediction
if st.button("ทำนาย"):
    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'stories': [stories],
        'mainroad': [mainroad],
        'guestroom': [guestroom],
        'basement': [basement],
        'hotwaterheating': [hotwaterheating],
        'airconditioning': [airconditioning],
        'parking': [parking],
        'prefarea': [prefarea],
        'furnishingstatus': [furnishingstatus]
    })

    # ทำการทำนาย
    predicted_price = model.predict(input_data)

    # แสดงผลลัพธ์
    st.write(f"ราคาที่คาดการณ์: {predicted_price[0]:,.2f} บาท")

    # สร้างกราฟ
    # สร้าง DataFrame สำหรับการแสดงผล
    actual_prices = [predicted_price[0]]  # ใช้ราคาที่ทำนายเป็นราคาจริงสำหรับการแสดง
    predicted_prices = [predicted_price[0]]  # ใช้ราคาที่ทำนาย

    results_df = pd.DataFrame({
        'Actual Price': actual_prices,
        'Predicted Price': predicted_prices
    })

    # สร้างกราฟ
    plt.figure(figsize=(10, 5))
    sns.barplot(data=results_df)
    plt.title('การเปรียบเทียบราคาจริงกับราคาที่ทำนาย')
    plt.ylabel('ราคา (บาท)')
    plt.xticks(rotation=0)
    st.pyplot(plt)
