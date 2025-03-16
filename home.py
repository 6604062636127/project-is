import streamlit as st
from navbar import navbar  # นำเข้า Navbar
from doc1 import app as app_doc1  # นำเข้าฟังก์ชัน app() จาก doc1
from doc2 import app as app_doc2  # นำเข้าฟังก์ชัน app() จาก doc2
from ML import app as app_ml  # นำเข้าฟังก์ชัน app() จาก ML
from NN import app as app_nn  # นำเข้าฟังก์ชัน app() จาก NN

# เรียกใช้ Navbar
navbar()

# อ่านค่าพารามิเตอร์จาก URL
query_params = st.query_params
page = query_params.get("page", "Home") 
st.session_state["page"] = page

# CSS สำหรับตกแต่ง
st.markdown("""
    <style>
        .title {
            color: #1E3A8A;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            font-family: 'Roboto', sans-serif;
        }
        .subtitle {
            color: #4A5568;
            font-size: 20px;
            text-align: center;
            margin-bottom: 20px;
            font-family: 'Arial', sans-serif;
        }
        .written{
            color: #4A5568;
            font-size: 20px;
            text-align: center;
            margin-bottom: 20px;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background: linear-gradient(135deg, #1E3A8A, #3B82F6);
            color: white;
            font-size: 16px;
            padding: 12px 24px;
            border-radius: 8px;
            border: none;
            transition: all 0.3s ease-in-out;
            font-weight: bold;
            letter-spacing: 1px;
        }
        .stButton>button:hover {
            background: #2563EB;
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:active {
            transform: scale(0.98);
        }
        .st-expanderHeader {
            background-color: #3B82F6;
            color: white;
            font-size: 18px;
            font-weight: bold;
        }
        .st-expanderContent {
            padding: 10px;
            background: #f3f4f6;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# แสดงหน้าที่เลือก
if page == "Home":
    st.markdown('<h1 class="title">🏠 Home Page</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Welcome to the Machine Learning & Neural Network!</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="written">เว็บไซต์นี้เป็นแพลตฟอร์มสำหรับการศึกษาและทดลองเกี่ยวกับ **Machine Learning (ML)** และ **Neural Networks (NN)**  
    สามารถดูเอกสารเกี่ยวกับ Machine Learning และ Neural Networks รวมถึงทดลองใช้งานโมเดลที่พัฒนาขึ้นมาได้จากเมนูด้านบน</p>""", unsafe_allow_html=True)


elif page == "ML":
    app_doc1()  # เรียกใช้ app จาก doc1
elif page == "NN":
    app_doc2()  # เรียกใช้ app จาก doc2
elif page == "Demo ML":
    app_ml()  # เรียกใช้ app จาก ML
elif page == "Demo NN":
    app_nn()  # เรียกใช้ app จาก NN
