import streamlit as st

# กำหนดธีมของ Streamlit ก่อนที่จะมีการเรียกใช้คำสั่งอื่น ๆ
st.set_page_config(page_title="ทำนายราคาบ้าน", layout="wide")

def app():
    # สไตล์ที่ปรับปรุงให้ทันสมัย
    st.markdown("""
        <style>
            /* พื้นหลัง */
            .main {
                background-color: #f5f7fb;
                font-family: 'Roboto', sans-serif;
            }

            /* หัวข้อหลัก */
            h1 {
                font-size: 2.8rem;
                color: #1F3A52;
                text-align: center;
                margin-top: 30px;
                margin-bottom: 20px;
                font-weight: bold;
            }

            /* หัวข้อย่อย */
            h2, h3 {
                font-size: 1.8rem;
                color: #2980B9;
                margin-bottom: 15px;
            }

            h3 {
                color: #1E4D87;
            }

            /* ข้อความ */
            p, li {
                color: #7F8C8D;
                font-size: 16px;
                line-height: 1.8;
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

            /* ชื่อหัวข้อหลัก */
            .title {
                font-size: 2.5rem;
                color: #1F3A52;
                font-weight: bold;
                text-align: center;
                margin-top: 30px;
                margin-bottom: 20px;
            }

            /* กล่องข้อความให้ความสำคัญ */
            .important-box {
                background-color: #D6EAF8;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 30px;
            }

        </style>
    """, unsafe_allow_html=True)

    # หัวข้อหลัก
    st.markdown('<h1 class="title">แนวทางการพัฒนา Machine Learning สำหรับการทำนายราคาบ้าน </h1>', unsafe_allow_html=True)

    # 1. ที่มาของ Dataset
    st.markdown('<h2>1. ที่มาของ Dataset</h2>', unsafe_allow_html=True)
    st.write("""
    - ดาวน์โหลด Dataset ที่ใช้ในโปรเจกต์นี้ได้จาก Kaggle 
    - ลิงค์ Dataset : [Kaggle Housing Prices](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)
    """)
    st.markdown('<h3>ชนิดของข้อมูล (Data Type)</h3>', unsafe_allow_html=True)
    st.write("""
    Housing Prices Dataset
    - 1. ข้อมูลเชิงตัวเลข เช่น ราคาบ้าน, ขนาด, จำนวนห้อง
    - 2. ข้อมูลเชิงหมวดหมู่ เช่น ประเภทของบ้าน, ทำเลที่ตั้ง, วัสดุก่อสร้าง""")

    # 2. รายละเอียดของ Dataset
    st.markdown('<h2>2. Feature ของ Dataset</h2>', unsafe_allow_html=True)
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

    # 3. การเตรียมข้อมูล (Data Preparation)
    st.markdown('<h2>3. การเตรียมข้อมูล (Data Preparation)</h2>', unsafe_allow_html=True)
    st.write("""
    - **การจัดการค่าที่หายไป** : เติมค่าที่หายไปด้วยค่ามัธยฐาน (Median) หรือค่าที่เหมาะสม
    - **การแปลงหน่วย** : แปลงพื้นที่จาก ตารางฟุต เป็น ตารางเมตร เพื่อให้ค่ามีความหมายมากขึ้น
    - **การเข้ารหัสฟีเจอร์เชิงหมวดหมู่** : ใช้ **One-Hot Encoding** และ **Label Encoding** สำหรับข้อมูลประเภทข้อความ
    - **การแบ่งข้อมูล** : แบ่งข้อมูลเป็นชุด **Train** และชุด **Test** (80:20)
    - **การปรับสเกลข้อมูล** : ใช้ Min-Max Scaling หรือ Standardization เพื่อทำให้ข้อมูลมีสเกลเดียวกัน
    """)

    # 4. ผลลัพธ์ของโมเดล
    st.markdown('<h2>4. ผลลัพธ์ของโมเดล</h2>', unsafe_allow_html=True)
    st.write("""
    - **Mean Absolute Error (MAE)** : 1,020,847.32 บาท
    - **Mean Absolute Percentage Error (MAPE)** : 21.79%
    - **พารามิเตอร์ที่ดีที่สุดจาก Grid Search** : 
            - max_depth: 10 
            - min_samples_split: 10 
            - n_estimators: 200
    """)

    # 5 . การวิเคราะห์ผลลัพธ์ (Model Evaluation)
    st.markdown('<h2>5. การวิเคราะห์ผลลัพธ์ (Model Evaluation)</h2>', unsafe_allow_html=True)
    st.write(""" 
    - **Linear Regression** : มีค่า R² สูงที่สุด (0.6529) ซึ่งแสดงว่าโมเดลนี้สามารถอธิบายความแปรปรวนในราคาบ้านได้ดีกว่าโมเดลอื่น ๆ
    - **Decision Tree** : มีค่า R² ต่ำที่สุด (0.4771) ซึ่งแสดงว่าโมเดลนี้ไม่สามารถอธิบายข้อมูลได้ดีนัก และมีค่า MSE สูงที่สุด ซึ่งหมายถึงความแม่นยำต่ำ
    - **Random Forest** : มีค่า MSE ที่ต่ำกว่า Decision Tree แต่สูงกว่า Linear Regression และมีค่า R² ที่อยู่ในระดับกลาง
    """)

    # 6. เหตุผลในการเลือกใช้ Random Forest สำหรับการทำนายราคาบ้าน
    st.markdown('<h2>6. เหตุผลในการเลือกใช้ Random Forest</h2>', unsafe_allow_html=True)
    st.write("""
    - **ความสามารถในการจัดการกับข้อมูลที่ซับซ้อน** : Random Forest ใช้การรวมผลจากหลาย ๆ ต้นไม้การตัดสินใจ (decision trees) ซึ่งช่วยให้สามารถจัดการกับความซับซ้อนและความไม่เป็นเชิงเส้น (non-linearity) ของข้อมูลได้ดีกว่าโมเดลเชิงเส้น
    - **ความแม่นยำที่สูงขึ้น** : Random Forest มีค่า Mean Squared Error (MSE) ที่ต่ำกว่า Decision Tree แสดงถึงความแม่นยำที่สูงกว่าในการทำนายราคาบ้าน
    - **การลด Overfitting** : Random Forest ช่วยลดปัญหา Overfitting โดยการสร้างหลาย ๆ ต้นไม้จากการสุ่มตัวอย่างข้อมูล
    - **ความยืดหยุ่น** : สามารถจัดการกับฟีเจอร์ทั้งเชิงหมวดหมู่ (categorical) และเชิงตัวเลข (numerical)
    - **การตีความผลลัพธ์** : Random Forest มีเครื่องมือในการวิเคราะห์ความสำคัญของฟีเจอร์ (feature importance) ช่วยให้เข้าใจว่าองค์ประกอบใดมีผลต่อการทำนายราคาบ้านมากที่สุด
    """)

if __name__ == "__main__":
    app()

