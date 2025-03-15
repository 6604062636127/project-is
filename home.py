import streamlit as st
from navbar import navbar  # import ฟังก์ชัน navbar

# ฟังก์ชันหลักที่แสดงหน้าแรก
def main():
    navbar()  # เรียกใช้ฟังก์ชัน navbar

# ฟังก์ชันเพื่อแสดงการทำงานของหน้าเว็บตาม session_state.page
def app():
    if "page" not in st.session_state:
        st.session_state.page = "home"  # ตั้งค่าเริ่มต้นหน้าเป็น "home"

    # ตรวจสอบว่าหน้าปัจจุบันคือหน้าไหน
    if st.session_state.page == "home":
        main()  # เรียกฟังก์ชัน main
    elif st.session_state.page == "page1":
        st.title("หน้า 1")
        st.write("คุณอยู่ในหน้า 1")
    elif st.session_state.page == "page2":
        st.title("หน้า 2")
        st.write("คุณอยู่ในหน้า 2")
    elif st.session_state.page == "page3":
        st.title("หน้า 3")
        st.write("คุณอยู่ในหน้า 3")
    elif st.session_state.page == "page4":
        st.title("หน้า 4")
        st.write("คุณอยู่ในหน้า 4")

# เรียกใช้ฟังก์ชัน app()
if __name__ == "__main__":
    app()
