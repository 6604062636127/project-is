import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
import pickle
import streamlit as st

# ฟังก์ชันสำหรับการโหลดโมเดล
def load_model():
    with open('random_forest_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# ฟังก์ชันสำหรับการทำนาย
def predict_price(model, input_data):
    predicted_price = model.predict(input_data)
    return predicted_price

# ฟังก์ชันสำหรับการสร้างกราฟ
def plot_results(y_test, predicted_prices):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=y_test, y=predicted_prices)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # เส้น 45 องศา
    plt.xlabel('ราคาจริง (บาท)')
    plt.ylabel('ราคาที่ทำนาย (บาท)')
    plt.title('การเปรียบเทียบราคาจริงกับราคาที่ทำนาย')
    plt.grid()
    st.pyplot(plt)

# สร้าง UI สำหรับ Streamlit
st.title("การทำนายราคาอสังหาริมทรัพย์")

# รับข้อมูลจากผู้ใช้
area_input = st.number_input("กรุณากรอกพื้นที่บ้าน (ตารางฟุต)", min_value=0.0)
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

# แปลงพื้นที่จากตารางฟุตเป็นตารางเมตร
area_in_square_meters = area_input * 0.092903

# แสดงพื้นที่ที่แปลงแล้ว
st.write(f"พื้นที่บ้านที่แปลงเป็นตารางเมตร: {area_in_square_meters:.2f} ตารางเมตร")

# โหลดโมเดล
model = load_model()

# สร้าง DataFrame สำหรับข้อมูลที่ป้อนเข้า
input_data = pd.DataFrame({
    'area': [area_in_square_meters],
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

# แปลงฟีเจอร์เชิงหมวดหมู่เป็นตัวเลข
input_data = pd.get_dummies(input_data, drop_first=True)

# สร้างปุ่มทำนายราคา
if st.button("ทำนายราคา"):
    # ทำการทำนายราคาโดยใช้โมเดลที่เตรียมไว้
    predicted_price = model.predict(input_data)  # ใช้ข้อมูลที่สร้างขึ้น
    st.write(f"ราคาที่คาดการณ์: {predicted_price[0]:.2f} บาท")
