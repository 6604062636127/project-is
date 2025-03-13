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
st.write("กรุณาอัปโหลดไฟล์ Housing.csv เพื่อเริ่มต้น")

# อัปโหลดไฟล์ CSV
uploaded_file = st.file_uploader("เลือกไฟล์ Housing.csv", type=["csv"])

if uploaded_file is not None:
    # อ่านข้อมูลจากไฟล์ CSV
    df = pd.read_csv(uploaded_file)

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

    # สร้างกราฟ
    plot_results(y, predicted_prices)
