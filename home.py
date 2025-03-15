import streamlit as st
from navbar import navbar  # นำเข้า Navbar
from doc1 import app as app_doc1  # นำเข้าฟังก์ชัน app() จาก doc1
from doc2 import app as app_doc2  # นำเข้าฟังก์ชัน app() จาก doc2
from ML import app as app_ml  # นำเข้าฟังก์ชัน app() จาก ML
from NN import app as app_nn  # นำเข้าฟังก์ชัน app() จาก NN

# เรียกใช้ Navbar
navbar()

# อ่านค่าพารามิเตอร์จาก URL
query_params = st.experimental_get_query_params()  # ใช้ experimental_get_query_params()
page = query_params.get("page", ["Home"])[0]  # Default to "Home"

# แสดงหน้าที่เลือก
if page == "Home":
    st.title("Home Page")
elif page == "Document ML":
    app_doc1()  # เรียกใช้ app จาก doc1
elif page == "Document NN":
    app_doc2()  # เรียกใช้ app จาก doc2
elif page == "Demo ML":
    app_ml()  # เรียกใช้ app จาก ML
elif page == "Demo NN":
    app_nn()  # เรียกใช้ app จาก NN
