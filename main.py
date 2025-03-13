import pandas as pd
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

# สร้าง UI สำหรับ Streamlit
st.title("การทำนายราคาอสังหาริมทรัพย์")

# รับข้อมูลพื้นที่บ้านจากผู้ใช้
area_input = st.number_input("กรุณากรอกพื้นที่บ้าน (ตารางฟุต)", min_value=0.0)

# แปลงพื้นที่จากตารางฟุตเป็นตารางเมตร
area_in_square_meters = area_input * 0.092903

# แสดงพื้นที่ที่แปลงแล้ว
st.write(f"พื้นที่บ้านที่แปลงเป็นตารางเมตร: {area_in_square_meters:.2f} ตารางเมตร")

# โหลดโมเดล
model = load_model()

# สร้าง DataFrame สำหรับข้อมูลที่ป้อนเข้า
input_data = pd.DataFrame({
    'area': [area_in_square_meters],
    # เพิ่มฟีเจอร์อื่น ๆ ที่โมเดลต้องการที่นี่
    # เช่น bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus
})

# แปลงฟีเจอร์เชิงหมวดหมู่เป็นตัวเลข
input_data = pd.get_dummies(input_data, drop_first=True)

# สร้างปุ่มทำนายราคา
if st.button("ทำนายราคา"):
    # ทำการทำนายราคาโดยใช้โมเดลที่เตรียมไว้
    predicted_price = predict_price(model, input_data)  # ใช้ข้อมูลที่สร้างขึ้น
    st.write(f"ราคาที่คาดการณ์: {predicted_price[0]:.2f} บาท")
