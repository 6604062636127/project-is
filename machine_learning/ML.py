import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

def app():
    st.title("House Price Prediction App")
    st.header("Input Feature")
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)
df = pd.read_csv('Housing.csv')
area = st.number_input("Area of the house (in square meters)", min_value=0.0)

input_data = pd.DataFrame({
    'area': [area]
})
model_columns = model.feature_names_in_
input_data = input_data.reindex(columns=model_columns, fill_value=0)

if st.button("Predict Price"):
    predicted_price = model.predict(input_data)
    st.write(f"The predicted house price is: {predicted_price[0]:.2f} บาท")

    st.subheader("Price Prediction Visualization")
    
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

    st.pyplot(plt)

st.write("กรุณากรอกข้อมูลด้านบนและคลิก 'Predict Price' เพื่อดูราคาที่คาดการณ์ไว้.")
