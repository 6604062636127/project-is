import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle
import streamlit as st
import os

# ฟังก์ชันสำหรับโหลดข้อมูล
def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"Error: The file {file_path} does not exist.")
        return None
    data = pd.read_csv(file_path)
    data.fillna(method='ffill', inplace=True)
    data = pd.get_dummies(data, drop_first=True)
    return data

# ฟังก์ชันสำหรับฝึกโมเดล
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = XGBRegressor(objective='reg:squarederror', random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write(f'XGBoost Mean Squared Error: {mse:.2f}')
    st.write(f'XGBoost R^2 Score: {r2:.2f}')

    return model

# ฟังก์ชันสำหรับบันทึกโมเดล
def save_model(model, filename):
    with open(filename, 'wb') as f:
        pickle.dump(model, f)

# ฟังก์ชันสำหรับโหลดโมเดล
def load_model(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# ฟังก์ชันหลัก
def main():
    # กำหนดที่อยู่ของไฟล์ CSV
    file_path = "Housing.csv"  # เปลี่ยนเป็นที่อยู่ของไฟล์ CSV ของคุณ

    # โหลดข้อมูล
    data = load_data(file_path)
    if data is None:
        return  # หยุดการทำงานหากไม่สามารถโหลดข้อมูลได้

    # แยกฟีเจอร์และเป้าหมาย
    X = data.drop('price', axis=1)
    y = data['price']

    # ฝึกโมเดล
    model = train_model(X, y)

    # บันทึกโมเดล
    save_model(model, 'model.pkl')

    # สร้างแอป Streamlit
    st.title('Housing Price Prediction App')

    # สร้างฟอร์มสำหรับรับข้อมูลจากผู้ใช้
    user_input = {}
    for column in X.columns:
        user_input[column] = st.number_input(f'Enter {column}', value=0)

    # แปลงข้อมูลผู้ใช้เป็น DataFrame
    input_df = pd.DataFrame([user_input])

    # โหลดโมเดลที่บันทึกไว้
    loaded_model = load_model('model.pkl')

    # ปุ่มทำนาย
    if st.button('Predict Price'):
        # ทำนายผล
        prediction = loaded_model.predict(input_df)

        # แสดงผลลัพธ์
        st.success(f'The estimated price of the house is: ${int(prediction[0]):,}')

if __name__ == "__main__":
    main()
