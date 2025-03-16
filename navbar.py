import streamlit as st
def navbar():
    # CSS สำหรับ Navbar แนวนอน
    st.markdown("""
        <style>
    /* Navbar หลัก */
    .navbar {
        background: linear-gradient(135deg, #1E3A8A, #3B82F6); /* ไล่สีให้ดูทันสมัย */
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 14px 24px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        border-radius: 12px;
        font-family: 'Poppins', sans-serif;
        margin-bottom: 20px;
    }

    /* ลิงก์ใน Navbar */
    .navbar a {
        color: white;
        text-decoration: none;
        padding: 12px 28px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 8px;
        margin: 0 12px;
        transition: all 0.3s ease-in-out;
        position: relative;
        overflow: hidden;
    }

    /* เอฟเฟกต์ไฮไลท์เมื่อ hover */
    .navbar a::before {
        content: "";
        position: absolute;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.2);
        top: 0;
        left: -100%;
        transition: left 0.3s ease-in-out;
    }

    .navbar a:hover::before {
        left: 0;
    }

    /* ลิงก์ที่กำลังใช้งาน */
    .navbar a.active {
        background: #4CAF50;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
</style>
    """, unsafe_allow_html=True)

    # สร้าง Navbar
    st.markdown("""
        <div class="navbar">
            <a href="/?page=Home" target="_self" class="active">🛖</a>
            <a href="/?page=ML" target="_self">Doc ML</a>
            <a href="/?page=Demo ML" target="_self">Demo ML</a>
            <a href="/?page=NN" target="_self">Doc NN</a>
            <a href="/?page=Demo NN" target="_self">Demo NN</a>
        </div>
    """, unsafe_allow_html=True)
