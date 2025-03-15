import streamlit as st

def navbar():
    # CSS สำหรับ Navbar แนวนอน
    st.markdown("""
        <style>
            .navbar {
                background-color: #333;
                overflow: hidden;
                display: flex;
                justify-content: center;
                padding: 10px;
            }
            .navbar a {
                color: white;
                text-decoration: none;
                padding: 14px 20px;
                font-size: 18px;
                font-weight: bold;
            }
            .navbar a:hover {
                background-color: #575757;
                border-radius: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # สร้าง Navbar
    st.markdown("""
        <div class="navbar">
            <a href="/?page=Home" target="_self">Home</a>
            <a href="/?page=Doc1" target="_self">Doc1</a>
            <a href="/?page=Doc2" target="_self">Doc2</a>
            <a href="/?page=ML" target="_self">ML</a>
            <a href="/?page=NN" target="_self">NN</a>
        </div>
    """, unsafe_allow_html=True)

    
