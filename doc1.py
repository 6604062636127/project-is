import streamlit as st

# กำหนดธีมของ Streamlit ก่อนที่จะมีการเรียกใช้คำสั่งอื่น ๆ
st.set_page_config(page_title="Predict House", layout="wide")

def app():
    # สไตล์ที่ปรับปรุงให้ทันสมัย
    st.markdown("""
        <style>
            /* พื้นหลัง */
            .main {
                background-color: #f5f7fb;
            }

            /* หัวข้อ */
            h1, h2, h3 {
                font-family: 'Roboto', sans-serif;
                font-weight: 700;
                color: #2C3E50;
            }

            /* ข้อความ */
            p {
                color: #7F8C8D;
                font-size: 18px;
                line-height: 1.6;
            }

            /* สไตล์ปุ่ม */
            .stButton>button {
                background-color: #3498DB;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                padding: 12px 24px;
                border: none;
                transition: all 0.3s ease;
            }

            .stButton>button:hover {
                background-color: #2980B9;
                transform: scale(1.05);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            }

            /* สไตล์ของหัวข้อหลัก */
            .title {
                color: #1F3A52;
                font-size: 2.5rem;
                text-align: center;
                font-family: 'Roboto', sans-serif;
                margin-top: 30px;
                margin-bottom: 20px;
            }

            /* สไตล์ของหัวข้อย่อย */
            .header {
                font-size: 2rem;
                color: #34495E;
                margin-bottom: 10px;
            }

            /* สไตล์ของกล่องข้อความ */
            .content-box {
                background-color: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
                margin-bottom: 20px;
                transition: transform 0.3s ease-in-out;
            }

            .content-box:hover {
                transform: scale(1.02);
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
            }

            /* สไตล์สำหรับข้อความที่มีการเน้น */
            .highlight {
                color: #3498DB;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # หัวข้อหลัก
    st.markdown('<h1 class="title">การทำนายราคาบ้านด้วย Machine Learning</h1>', unsafe_allow_html=True)

    # 1. ที่มาของ Dataset
    st.markdown('<div class="header">1. ที่มาของ Dataset</div>', unsafe_allow_html=True)
    st.write("""
    - Dataset ที่ใช้ในโปรเจกต์นี้สามารถดาวน์โหลดได้จาก Kaggle 
    - ลิงค์ Dataset : https://www.kaggle.com/datasets/yasserh/housing-prices-dataset
    """)

    # 2. รายละเอียดของ Dataset
    st.markdown('<div class="header">2. รายละเอียดของ Dataset</div>', unsafe_allow_html=True)
    st.write("""
    - **price** : ราคาของบ้าน (เป้าหมายที่ต้องทำนาย เนื่องจากมีผลต่อราคาบ้านมากที่สุด)
    - **area** : ขนาดพื้นที่ของบ้าน (ตารางเมตร)
    - **bedrooms** : จำนวนห้องนอน
    - **bathrooms** : จำนวนห้องน้ำ
    - **stories** : จำนวนชั้นของบ้าน
    - **parking** : จำนวนที่จอดรถ
    - **prefarea** : บ้านอยู่ในทำเลที่ดีหรือไม่ (Yes/No)
    - **airconditioning** : มีเครื่องปรับอากาศหรือไม่ (Yes/No)
    - **furnishingstatus** : สถานะเฟอร์นิเจอร์ (Furnished/Semi-Furnished/Unfurnished)
    """)

    # 3. กระบวนการเตรียมข้อมูล
    st.markdown('<div class="header">3. กระบวนการเตรียมข้อมูล</div>', unsafe_allow_html=True)
    st.write("""
    - **การจัดการค่าที่หายไป** : เติมค่าที่หายไปด้วยค่ามัธยฐาน (Median) หรือค่าที่เหมาะสม
    - **การแปลงหน่วย** : แปลงพื้นที่จาก ตารางฟุต เป็น ตารางเมตร เพื่อให้ค่ามีความหมายมากขึ้น
    - **การเข้ารหัสฟีเจอร์เชิงหมวดหมู่** : ใช้ **One-Hot Encoding** และ **Label Encoding** สำหรับข้อมูลประเภทข้อความ
    - **การแบ่งข้อมูล** : แบ่งข้อมูลเป็นชุด **Train** และชุด **Test** (80:20)
    - **การปรับสเกลข้อมูล** : ใช้ Min-Max Scaling หรือ Standardization เพื่อทำให้ข้อมูลมีสเกลเดียวกัน
    """)

    # 4. ผลลัพธ์ของโมเดล
    st.markdown('<div class="header">4. ผลลัพธ์ของโมเดล</div>', unsafe_allow_html=True)
    st.write("""
    - **Mean Absolute Error (MAE)** : 1,020,847.32 บาท
    - **Mean Absolute Percentage Error (MAPE)** : 21.79%
    - **พารามิเตอร์ที่ดีที่สุดจาก Grid Search** : 
            - max_depth: 10 
            - min_samples_split: 10 
            - n_estimators': 200}
    """)

    # 5 . การวิเคราะห์ผลลัพธ์
    st.markdown('<div class="header">5. การวิเคราะห์ผลลัพธ์</div>', unsafe_allow_html=True)
    st.write(""" 
    - **Linear Regression** : มีค่า R² สูงที่สุด (0.6529) ซึ่งแสดงว่าโมเดลนี้สามารถอธิบายความแปรปรวนในราคาบ้านได้ดีกว่าโมเดลอื่น ๆ
    - **Decision Tree** : มีค่า R² ต่ำที่สุด (0.4771) ซึ่งแสดงว่าโมเดลนี้ไม่สามารถอธิบายข้อมูลได้ดีนัก และมีค่า MSE สูงที่สุด ซึ่งหมายถึงความแม่นยำต่ำ
    - **Random Forest** : มีค่า MSE ที่ต่ำกว่า Decision Tree แต่สูงกว่า Linear Regression และมีค่า R² ที่อยู่ในระดับกลาง
    """)

    # 6. เหตุผลในการเลือกใช้ Random Forest สำหรับการทำนายราคาบ้าน
    st.markdown('<div class="header">6. เหตุผลในการเลือกใช้ Random Forest</div>', unsafe_allow_html=True)
    st.write("""
    - **ความสามารถในการจัดการกับข้อมูลที่ซับซ้อน** : Random Forest ใช้การรวมผลจากหลาย ๆ ต้นไม้การตัดสินใจ (decision trees) ซึ่งช่วยให้สามารถจัดการกับความซับซ้อนและความไม่เป็นเชิงเส้น (non-linearity) ของข้อมูลได้ดีกว่าโมเดลเชิงเส้น
    - **ความแม่นยำที่สูงขึ้น** : Random Forest มีค่า Mean Squared Error (MSE) ที่ต่ำกว่า Decision Tree แสดงถึงความแม่นยำที่สูงกว่าในการทำนายราคาบ้าน
    - **การลด Overfitting** : Random Forest ช่วยลดปัญหา Overfitting โดยการสร้างหลาย ๆ ต้นไม้จากการสุ่มตัวอย่างข้อมูล
    - **ความยืดหยุ่น** : สามารถจัดการกับฟีเจอร์ทั้งเชิงหมวดหมู่ (categorical) และเชิงตัวเลข (numerical)
    - **การตีความผลลัพธ์** : Random Forest มีเครื่องมือในการวิเคราะห์ความสำคัญของฟีเจอร์ (feature importance) ช่วยให้เข้าใจว่าองค์ประกอบใดมีผลต่อการทำนายราคาบ้านมากที่สุด
    """)

if __name__ == "__main__":
    app()
