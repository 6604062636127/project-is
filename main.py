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

# รับข้อมูลพื้นที่บ้านจากผู้ใช้
area_input = st.number_input("กรุณากรอกพื้นที่บ้าน (ตารางฟุต)", min_value=0.0)

# แปลงพื้นที่จากตารางฟุตเป็นตารางเมตร
area_in_square_meters = area_input * 0.092903

# แสดงพื้นที่ที่แปลงแล้ว
st.write(f"พื้นที่บ้านที่แปลงเป็นตารางเมตร: {area_in_square_meters:.2f} ตารางเมตร")

# อ่านข้อมูลจากไฟล์ CSV โดยตรง
df = pd.read_csv('Housing.csv')

# แปลงพื้นที่จากตารางฟุตเป็นตารางเมตร
df['area'] = df['area'] * 0.092903

# เตรียมข้อมูล
X = df.drop('price', axis=1)  # ฟีเจอร์ทั้งหมด ยกเว้นราคา
y = df['price']  # ราคาบ้าน

# แปลงฟีเจอร์เชิงหมวดหมู่เป็นตัวเลข
X = pd.get_dummies(X, drop_first=True)

# โหลดโมเดล
model = load_model()

# ทำนายราคาบ้าน
predicted_prices = predict_price(model, X)

# คำนวณค่าความผิดพลาด
mae = mean_absolute_error(y, predicted_prices)
mape = mean_absolute_percentage_error(y, predicted_prices)

# แสดงผลลัพธ์
st.write(f'Mean Absolute Error (MAE): {mae:.2f} บาท')
st.write(f'Mean Absolute Percentage Error (MAPE): {mape:.2%}')

# สร้างปุ่มทำนายราคา
if st.button("ทำนายราคา"):
    # สร้าง DataFrame สำหรับข้อมูลที่ป้อนเข้า
    input_data = pd.DataFrame({
        'area': [area_in_square_meters],
        # เพิ่มฟีเจอร์อื่น ๆ ที่โมเดลต้องการที่นี่
        # เช่น bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus
    })

    # แปลงฟีเจอร์เชิงหมวดหมู่เป็นตัวเลข
    input_data = pd.get_dummies(input_data, drop_first=True)

    # ทำการทำนายราคาโดยใช้โมเดลที่เตรียมไว้
    predicted_price = model.predict(input_data)  # ใช้ข้อมูลที่สร้างขึ้น
   
