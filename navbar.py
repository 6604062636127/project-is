import streamlit as st
# Navbar UI
def navbar():
    st.markdown("""
        <style>
        .nav-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 20px;
        }
        .nav-btn {
            background: linear-gradient(135deg, #1E3A8A, #3B82F6);
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .nav-btn:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: scale(1.05);
        }
        .nav-active {
            background: #4CAF50 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    
    pages = ["Home", "Doc ML", "Demo ML", "Doc NN", "Demo NN"]
    for page in pages:
        is_active = "nav-btn nav-active" if st.session_state["page"] == page else "nav-btn"
        if st.button(page, key=page, on_click=set_page, args=(page,)):
            pass  # ใช้ session_state จัดการเปลี่ยนหน้า

    st.markdown('</div>', unsafe_allow_html=True)

# เรียกใช้ Navbar
navbar()

# แสดงผลลัพธ์ของแต่ละหน้า
st.write(f"### คุณกำลังอยู่ที่หน้า: {st.session_state['page']}")
