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
        .content-box {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .title {
            color: #1E3A8A;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }
        .subtitle {
            color: #4A5568;
            font-size: 20px;
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton>button {
            background: linear-gradient(135deg, #1E3A8A, #3B82F6);
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background: #2563EB;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# แสดงหน้าที่เลือก
if page == "Home":
    st.markdown('<h1 class="title">🏠 Home Page</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Welcome to the Machine Learning & Neural Network Dashboard!</p>', unsafe_allow_html=True)

    # กล่องข้อมูล
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.write("""
        เว็บไซต์นี้เป็นแพลตฟอร์มสำหรับการศึกษาและทดลองเกี่ยวกับ **Machine Learning (ML)** และ **Neural Networks (NN)**  
        สามารถดูเอกสารเกี่ยวกับ Machine Learning และ Neural Networks รวมถึงทดลองใช้งานโมเดลที่พัฒนาขึ้นมาได้จากเมนูด้านบน  
    """)
    
    # ปุ่มนำทาง
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄 ดูเอกสาร ML & NN"):
            st.experimental_set_query_params(page="ML")

    with col2:
        if st.button("🛠️ ทดลองใช้งานโมเดล"):
            st.experimental_set_query_params(page="Demo ML")

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "ML":
    app_doc1()  # เรียกใช้ app จาก doc1
elif page == "NN":
    app_doc2()  # เรียกใช้ app จาก doc2
elif page == "Demo ML":
    app_ml()  # เรียกใช้ app จาก ML
elif page == "Demo NN":
    app_nn()  # เรียกใช้ app จาก NN
