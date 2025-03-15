import streamlit as st
def navbar():
    # CSS สำหรับ Navbar แนวนอน
    st.markdown("""
        <style>
            /* Navbar หลัก */
            .navbar {
                background-color: #1E3A8A; /* สีพื้นหลังฟ้าเข้ม */
                overflow: hidden;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 12px 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* เงาสวยงาม */
                border-radius: 8px; /* มุมมน */
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            /* ลิงก์ใน Navbar */
            .navbar a {
                color: white;
                text-decoration: none;
                padding: 12px 24px;
                font-size: 18px;
                font-weight: 500;
                border-radius: 6px;
                margin: 0 10px;
                transition: background-color 0.3s, transform 0.3s; /* การเปลี่ยนสีพื้นหลังและการแสดงผล */
            }

            /* ลิงก์เมื่อ Hover */
            .navbar a:hover {
                background-color: #4CAF50; /* สีพื้นหลังเมื่อ hover */
                transform: scale(1.1); /* ขยายเล็กน้อยเมื่อ hover */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* เพิ่มเงาเมื่อ hover */
            }

            /* ลิงก์ที่กำลังใช้งาน */
            .navbar a.active {
                background-color: #3B82F6; /* สีพื้นหลังสำหรับลิงก์ที่ใช้งานอยู่ (สีน้ำเงิน) */
                font-weight: bold;
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
