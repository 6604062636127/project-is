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
# แปลงพื้นที่จากตารางฟุตเป็นตารางเมตร
area_in_square_meters = area_input * 0.092903

# แสดงพื้นที่ที่แปลงแล้ว
st.write(f"พื้นที่บ้านที่แปลงเป็นตารางเมตร: {area_in_square_meters:.2f} ตารางเมตร")

# โหลดโมเดล
model = load_model()

# สร้าง DataFrame สำหรับข้อมูลที่ป้อนเข้า
input_data = pd.DataFrame({
    'area': [area_in_square_meters],
})

# สร้างปุ่มทำนายราคา
if st.button("ทำนายราคา"):
    # ทำการทำนายราคาโดยใช้โมเดลที่เตรียมไว้
    predicted_price = model.predict(input_data)  # ใช้ข้อมูลที่สร้างขึ้น
    st.write(f"ราคาที่คาดการณ์: {predicted_price[0]:.2f} บาท")
