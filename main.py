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
    X = data[['Area', 'Bedrooms', 'Bathrooms', 'Parking', 'mainroad_yes', 'guestroom_yes', 
               'basement_yes', 'hotwaterheating_yes', 'airconditioning_yes', 
               'prefarea_yes', 'furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished']]
    y = data['price']

    # ฝึกโมเดล
    model = train_model(X, y)

    # บันทึกโมเดล
    save_model(model, 'model.pkl')

    # สร้างแอป Streamlit
    st.title('Housing Price Prediction App')

    # สร้างฟอร์มสำหรับรับข้อมูลจากผู้ใช้
    area = st.number_input('Enter Area (in sq ft)', value=0)
    bedrooms = st.number_input('Enter Number of Bedrooms', value=0)
    bathrooms = st.number_input('Enter Number of Bathrooms', value=0)
    parking = st.number_input('Enter Number of Parking Spaces', value=0)

    # ค่าบูลีน
    mainroad_yes = st.radio('Is the house near the main road?', ('No', 'Yes'))
    guestroom_yes = st.radio('Does the house have a guest room?', ('No', 'Yes'))
    basement_yes = st.radio('Does the house have a basement?', ('No', 'Yes'))
    hotwaterheating_yes = st.radio('Does the house have hot water heating?', ('No', 'Yes'))
    airconditioning_yes = st.radio('Does the house have air conditioning?', ('No', 'Yes'))
    prefarea_yes = st.radio('Is the house in a preferred area?', ('No', 'Yes'))
    furnishingstatus_semi_furnished = st.radio('Is the house semi-furnished?', ('No', 'Yes'))
    furnishingstatus_unfurnished = st.radio('Is the house unfurnished?', ('No', 'Yes'))

      # แปลงค่าบูลีนเป็น 0 หรือ 1
    mainroad_yes = 1 if mainroad_yes == 'Yes' else 0
    guestroom_yes = 1 if guestroom_yes == 'Yes' else 0
    basement_yes = 1 if basement_yes == 'Yes' else 0
    hotwaterheating_yes = 1 if hotwaterheating_yes == 'Yes' else 0
    airconditioning_yes = 1 if airconditioning_yes == 'Yes' else 0
    prefarea_yes = 1 if prefarea_yes == 'Yes' else 0
    furnishingstatus_semi_furnished = 1 if furnishingstatus_semi_furnished == 'Yes' else 0
    furnishingstatus_unfurnished = 1 if furnishingstatus_unfurnished == 'Yes' else 0
    # ปุ่มทำนาย
    if st.button('Predict Price'):
        # โหลดโมเดลที่บันทึกไว้
        loaded_model = load_model('model.pkl')

        # แปลงข้อมูลผู้ใช้เป็น DataFrame
        input_df = pd.DataFrame([[area, bedrooms, bathrooms, parking, mainroad_yes, guestroom_yes,
                                   basement_yes, hotwaterheating_yes, airconditioning_yes,
                                   prefarea_yes, furnishingstatus_semi_furnished, furnishingstatus_unfurnished]],
                                 columns=['Area', 'Bedrooms', 'Bathrooms', 'Parking', 'mainroad_yes',
                                          'guestroom_yes', 'basement_yes', 'hotwaterheating_yes',
                                          'airconditioning_yes', 'prefarea_yes',
                                          'furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished'])

        # ทำนายผล
        prediction = loaded_model.predict(input_df)

        # แสดงผลลัพธ์
        st.success(f'The estimated price of the house is: ${int(prediction[0]):,}')

if __name__ == "__main__":
    main()
