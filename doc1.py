import streamlit as st

# กำหนดธีมของ Streamlit ก่อนที่จะมีการเรียกใช้คำสั่งอื่น ๆ
st.set_page_config(page_title="การทำนายราคาบ้าน", layout="wide")

def app():
    # สไตล์ที่ปรับปรุงให้ทันสมัย
    st.markdown("""
        <style>
            .main {
                background-color: #f0f4f8;
            }
            h2 {
                color: #2C3E50;
                font-family: 'Arial', sans-serif;
            }
            h3 {
                color: #34495E;
            }
            p {
                color: #7F8C8D;
                font-size: 18px;
            }
            .stButton>button {
                background-color: #3498DB;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 5px;
            }
            .stButton>button:hover {
                background-color: #2980B9;
            }
        </style>
    """, unsafe_allow_html=True)

    # หัวข้อหลัก
    st.title("การทำนายราคาบ้านด้วย Machine Learning")

    # 1. ที่มาของ Dataset
    st.header("1. ที่มาของ Dataset")
    st.write("""
    - Dataset ที่ใช้ในโปรเจกต์นี้สามารถดาวน์โหลดได้จาก Kaggle 
    - ลิงค์ Dataset : https://www.kaggle.com/datasets/yasserh/housing-prices-dataset
    """)

    # 2. รายละเอียดของ Dataset
    st.header("2. รายละเอียดของ Dataset")
    st.write("""
    - **price**: ราคาของบ้าน (เป้าหมายที่ต้องทำนาย เนื่องจากมีผลต่อราคาบ้านมากที่สุด)
    - **area**: ขนาดพื้นที่ของบ้าน (ตารางเมตร)
    - **bedrooms**: จำนวนห้องนอน
    - **bathrooms**: จำนวนห้องน้ำ
    - **stories**: จำนวนชั้นของบ้าน
    - **parking**: จำนวนที่จอดรถ
    - **prefarea**: บ้านอยู่ในทำเลที่ดีหรือไม่ (Yes/No)
    - **airconditioning**: มีเครื่องปรับอากาศหรือไม่ (Yes/No)
    - **furnishingstatus**: สถานะเฟอร์นิเจอร์ (Furnished/Semi-Furnished/Unfurnished)
    """)

    # 3. กระบวนการเตรียมข้อมูล
    st.header("3. กระบวนการเตรียมข้อมูล")
    st.write("""
    - **การจัดการค่าที่หายไป**: เติมค่าที่หายไปด้วยค่ามัธยฐาน (Median) หรือค่าที่เหมาะสม
    - **การแปลงหน่วย**: แปลงพื้นที่จาก ตารางฟุต เป็น ตารางเมตร เพื่อให้ค่ามีความหมายมากขึ้น
    - **การเข้ารหัสฟีเจอร์เชิงหมวดหมู่**: ใช้ One-Hot Encoding และ Label Encoding สำหรับข้อมูลประเภทข้อความ
    - **การแบ่งข้อมูล**: แบ่งข้อมูลเป็นชุด Train และชุด Test (80:20)
    - **การปรับสเกลข้อมูล**: ใช้ Min-Max Scaling หรือ Standardization เพื่อทำให้ข้อมูลมีสเกลเดียวกัน
    """)

    # 4. ผลลัพธ์ของโมเดล
    st.header("4. ผลลัพธ์ของโมเดล")
    st.write("""
    - **Mean Absolute Error (MAE)**: 1,020,847.32 บาท
    - **Mean Absolute Percentage Error (MAPE)**: 21.79%
    - **พารามิเตอร์ที่ดีที่สุดจาก Grid Search**: 
            - max_depth: 10 
            - min_samples_split: 10 
            - n_estimators': 200}
    """)

    # 5 . การวิเคราะห์ผลลัพธ์
    st.header("6. การวิเคราะห์ผลลัพธ์")
    st.write(""" 
    - **Linear Regression** มีค่า R² สูงที่สุด (0.6529) ซึ่งแสดงว่าโมเดลนี้สามารถอธิบายความแปรปรวนในราคาบ้านได้ดีกว่าโมเดลอื่น ๆ
    - **Decision Tree** มีค่า R² ต่ำที่สุด (0.4771) ซึ่งแสดงว่าโมเดลนี้ไม่สามารถอธิบายข้อมูลได้ดีนัก และมีค่า MSE สูงที่สุด ซึ่งหมายถึงความแม่นยำต่ำ
    - **Random Forest** มีค่า MSE ที่ต่ำกว่า Decision Tree แต่สูงกว่า Linear Regression และมีค่า R² ที่อยู่ในระดับกลาง
    """)

    # 6. เหตุผลในการเลือกใช้ Random Forest สำหรับการทำนายราคาบ้าน
    st.header("6. เหตุผลในการเลือกใช้ Random Forest")
    st.write("""
    - 1. **ความสามารถในการจัดการกับข้อมูลที่ซับซ้อน**: Random Forest ใช้การรวมผลจากหลาย ๆ ต้นไม้การตัดสินใจ (decision trees) ซึ่งช่วยให้สามารถจัดการกับความซับซ้อนและความไม่เป็นเชิงเส้น (non-linearity) ของข้อมูลได้ดีกว่าโมเดลเชิงเส้น
    - 2. **ความแม่นยำที่สูงขึ้น**: Random Forest มีค่า Mean Squared Error (MSE) ที่ต่ำกว่า Decision Tree แสดงถึงความแม่นยำที่สูงกว่าในการทำนายราคาบ้าน
    - 3. **การลด Overfitting**: Random Forest ช่วยลดปัญหา Overfitting โดยการสร้างหลาย ๆ ต้นไม้จากการสุ่มตัวอย่างข้อมูล
    - 4. **ความยืดหยุ่น**: สามารถจัดการกับฟีเจอร์ทั้งเชิงหมวดหมู่ (categorical) และเชิงตัวเลข (numerical)
    - 5. **การตีความผลลัพธ์**: Random Forest มีเครื่องมือในการวิเคราะห์ความสำคัญของฟีเจอร์ (feature importance) ช่วยให้เข้าใจว่าองค์ประกอบใดมีผลต่อการทำนายราคาบ้านมากที่สุด
    """)

if __name__ == "__main__":
    app()
