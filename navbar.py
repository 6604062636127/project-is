import streamlit as st
def navbar():
    # CSS สำหรับ Navbar แนวนอน
    st.markdown("""
        <style>
            .navbar {
                background-color: #4CAF50; /* สีพื้นหลัง */
                overflow: hidden;
                display: flex;
                justify-content: center;
                padding: 10px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* เงา */
                border-radius: 5px; /* มุมมน */
            }
            .navbar a {
                color: white;
                text-decoration: none;
                padding: 14px 20px;
                font-size: 18px;
                font-weight: bold;
                transition: background-color 0.3s; /* การเปลี่ยนสีพื้นหลัง */
            }
            .navbar a:hover {
                background-color: #45a049; /* สีพื้นหลังเมื่อ hover */
                border-radius: 5px;
            }
            .navbar a.active {
                background-color: #3e8e41; /* สีพื้นหลังสำหรับลิงก์ที่ใช้งานอยู่ */
            }
        </style>
    """, unsafe_allow_html=True)

    # สร้าง Navbar
    st.markdown("""
        <div class="navbar">
            <a href="/?page=Home" target="_self" class="active">Home</a>
            <a href="/?page=Doc1" target="_self">Document ML</a>
            <a href="/?page=Doc2" target="_self">Demo Machine Learning</a>
            <a href="/?page=ML" target="_self">Document NN</a>
            <a href="/?page=NN" target="_self">Neural Network</a>
        </div>
    """, unsafe_allow_html=True)
