import streamlit as st
from navbar import navbar  # นำเข้า Navbar
from machine_learning import doc1, ML  # นำเข้าหน้าในโฟลเดอร์ machine_learning
from neural_network import doc2, NN  # นำเข้าหน้าในโฟลเดอร์ neural_network

# เรียกใช้ Navbar
navbar()
# อ่านค่าพารามิเตอร์จาก URL
query_params = st.query_params
page = query_params.get("page", "Home")  # Default to "Home"

# แสดงหน้าที่เลือก
if page == "Home":
    st.title("Home Page")
elif page == "Document ML":
    doc1.app()
elif page == "Document NN":
    doc2.app()
elif page == "Demo ML":
    ML.app()
elif page == "Demo NN":
    NN.app()

