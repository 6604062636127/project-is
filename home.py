import streamlit as st

def app():
    st.title("Intelligence System")
    st.write("Welcome to our project!")
import streamlit as st

def main():
    st.title("หน้าแรก")
    st.write("ยินดีต้อนรับสู่หน้าแรกของแอป Streamlit ของคุณ!")

    # ลิงก์ไปยังหน้าอื่น
    if st.button("ไปยังหน้า 1"):
        st.session_state.page = "page1"
        st.experimental_rerun()
    if st.button("ไปยังหน้า 2"):
        st.session_state.page = "page2"
        st.experimental_rerun()
    if st.button("ไปยังหน้า 3"):
        st.session_state.page = "page3"
        st.experimental_rerun()
    if st.button("ไปยังหน้า 4"):
        st.session_state.page = "page4"
        st.experimental_rerun()

if __name__ == "__main__":
    main()
