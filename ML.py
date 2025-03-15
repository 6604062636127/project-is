import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

def app():
    # Title and header
    st.title("House Price Prediction App")
    st.header("Input Feature")

    # โหลดโมเดลจากไฟล์
    with open('random_forest_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # โหลดข้อมูลจากไฟล์ CSV
    df = pd.read_csv('Housing.csv')
    
    # รับข้อมูลจากผู้ใช้
    area = st.number_input("Area of the house (in square meters)", min_value=0.0)
    
    # เตรียมข้อมูลที่ผู้ใช้กรอก
    input_data = pd.DataFrame({
        'area': [area]
    })
    
    # ใช้ฟีเจอร์ของโมเดลในการสร้างข้อมูล
    model_columns = model.feature_names_in_
    input_data = input_data.reindex(columns=model_columns, fill_value=0)

    # เมื่อผู้ใช้คลิกปุ่ม "Predict Price"
    if st.button("Predict Price"):
        predicted_price = model.predict(input_data)
        
        # แสดงราคาที่คาดการณ์
        st.write(f"The predicted house price is: {predicted_price[0]:.2f} บาท")

        # ส่วนของการแสดงกราฟ
        st.subheader("Price Prediction Visualization")
        
        # สร้างกราฟ
        plt.figure(figsize=(10, 5))
        plt.scatter(df['area'], df['price'], color='gray', label='Actual Prices', alpha=0.5)  # แสดงราคาจริง
        plt.scatter(area, predicted_price, color='blue', s=100, label='Predicted Price')  # แสดงราคาที่คาดการณ์
        plt.xlabel('Area (square meters)')
        plt.ylabel('Price (Baht)')
        plt.title('House Price Prediction Based on Area')
        plt.xlim(0, df['area'].max() * 1.2)  # ขยายขอบเขต X-axis
        plt.ylim(0, predicted_price[0] * 1.2)  # ขยายขอบเขต Y-axis
        plt.grid()
        plt.legend()

        # แสดงกราฟใน Streamlit
        st.pyplot(plt)

    # ข้อความอธิบายการใช้งาน
    st.write("กรุณากรอกข้อมูลด้านบนและคลิก 'Predict Price' เพื่อดูราคาที่คาดการณ์ไว้.")
