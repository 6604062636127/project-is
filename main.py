import streamlit as st
import joblib

# โหลดไฟล์ House.pkl
model = joblib.load('House.pkl')

# แสดงโมเดลที่โหลด
print(model)

# แสดงโมเดลที่โหลดใน Streamlit
st.write(model)
