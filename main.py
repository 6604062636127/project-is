import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# หัวข้อหลัก
st.title("ยินดีต้อนรับสู่แอป Streamlit ของฉัน!")

# ส่วนสำหรับรับข้อมูลจากผู้ใช้
user_name = st.text_input("กรุณากรอกชื่อของคุณ:")
if user_name:
    st.write(f"สวัสดี, {user_name}!")

# ส่วนสำหรับแสดงข้อมูล
st.header("ข้อมูลที่น่าสนใจ")
st.write("นี่คือข้อมูลที่น่าสนใจเกี่ยวกับ Streamlit:")

# แสดงกราฟหรือข้อมูลเพิ่มเติม
st.line_chart([1, 2, 3, 4, 5])

# ส่วนสำหรับแสดงบล็อก
st.subheader("บล็อกยอดนิยม")
blogs = [
    {"title": "บล็อก 1", "url": "https://example.com/blog1"},
    {"title": "บล็อก 2", "url": "https://example.com/blog2"},
    {"title": "บล็อก 3", "url": "https://example.com/blog3"},
]

for blog in blogs:
    st.markdown(f"- [{blog['title']}]({blog['url']})")

# ส่วนท้าย
st.write("ขอบคุณที่เข้าชมแอปของเรา!")
