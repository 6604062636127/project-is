import streamlit as st
def navbar():
    # CSS สำหรับ Navbar แนวนอน
    st.markdown("""
       <style>
        /* พื้นหลังหลักของเว็บ */
        body {{
            background-color: #ffffff !important; /* พื้นหลังสีขาว */
        }}

        /* Navbar หลัก */
        .navbar-container {{
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }}

        .navbar {{
            background: #ffffff; /* พื้นหลังสีขาว */
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 14px 24px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* เงาเบาๆ */
            border-radius: 12px;
            font-family: 'Poppins', sans-serif;
            border: 1px solid #ddd; /* ขอบบางๆ */
            width: 80%;
            max-width: 900px;
        }}

        /* ลิงก์ใน Navbar */
        .navbar a {{
            color: #1E3A8A;
            text-decoration: none;
            padding: 12px 28px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 8px;
            margin: 0 12px;
            transition: all 0.3s ease-in-out;
            position: relative;
            overflow: hidden;
        }}

        /* เอฟเฟกต์ hover */
        .navbar a:hover {{
            background: rgba(62, 130, 255, 0.2);
            transform: scale(1.05);
        }}

        /* ลิงก์ที่กำลังใช้งาน */
        .navbar a.active {{
            background: #4CAF50;
            color: white;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }}
        </style>
    """, unsafe_allow_html=True)

    # สร้าง Navbar
    st.markdown("""
        <div class="navbar">
            <a href="/?page=Home" target="_self" class="active">Home</a>
            <a href="/?page=ML" target="_self">Doc ML</a>
            <a href="/?page=Demo ML" target="_self">Demo ML</a>
            <a href="/?page=NN" target="_self">Doc NN</a>
            <a href="/?page=Demo NN" target="_self">Demo NN</a>
        </div>
    """, unsafe_allow_html=True)
