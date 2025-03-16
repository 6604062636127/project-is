import streamlit as st

def app():
    # การปรับแต่งสไตล์ให้ทันสมัยและอ่านง่าย
    st.markdown("""
        <style>
            /* พื้นหลัง */
            .main {
                background-color: #f5f7fb;
            }

            /* หัวข้อหลัก */
            h1, h2, h3 {
                font-family: 'Roboto', sans-serif;
                font-weight: 700;
                color: #2C3E50;
                line-height: 1.4;
            }

            /* หัวข้อย่อย */
            h2 {
                font-size: 1.8rem;
                color: #34495E;
                margin-bottom: 15px;
            }

            h3 {
                font-size: 1.5rem;
                color: #2980B9;
                margin-top: 20px;
                margin-bottom: 10px;
            }

            /* ข้อความ */
            p, li {
                color: #7F8C8D;
                font-size: 16px;
                line-height: 1.8;
            }

            /* เพิ่มระยะห่างระหว่างข้อความ */
            .content-box {
                margin-top: 30px;
                padding: 20px;
                background-color: white;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease-in-out;
            }

            .content-box:hover {
                transform: scale(1.02);
                box-shadow: 0 6px 25px rgba(0, 0, 0, 0.15);
            }

            /* สไตล์ของปุ่ม */
            .stButton>button {
                background-color: #3498DB;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 24px;
                border-radius: 8px;
                border: none;
                transition: all 0.3s ease;
            }

            .stButton>button:hover {
                background-color: #2980B9;
                transform: scale(1.05);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            }

            /* เพิ่มเส้นขอบในแต่ละหัวข้อ */
            hr {
                border: 1px solid #BDC3C7;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("แนวทางการพัฒนา Neural Network สำหรับแยกเพศจากภาพ")

    st.header("1. การเตรียมข้อมูล (Data Preparation)")
    st.subheader("ฟีเจอร์ของ Dataset")
    st.write("""
    ### ที่มา  
    🔗 ดาวน์โหลด Dataset จาก Kaggle https://www.kaggle.com/datasets/humairmunir/gender-recognizer 

    ### ชนิดของข้อมูล (Data Type)  
    - Dataset ประกอบด้วย **ไฟล์ภาพ** (รูปภาพของผู้ชายและผู้หญิง)  
    - ใช้เพื่อให้โมเดลเรียนรู้และทำนายเพศจากภาพ  
    - ขนาดของไฟล์ภาพ **ไม่เท่ากัน** แต่ในโค้ดได้ **ปรับขนาดเป็น 128x128 พิกเซล** ก่อนนำเข้าโมเดล  

    ### การแบ่งข้อมูล (Data Split)  
    Dataset ถูกแบ่งออกเป็น 3 ชุดหลัก:  
    - **Training Data (Train)**: ใช้ฝึกโมเดล (**70%**)  
    - **Validation Data (Validation)**: ใช้ตรวจสอบโมเดลระหว่างฝึก (**15%**)  
    - **Test Data (Test)**: ใช้ทดสอบโมเดลหลังจากฝึกเสร็จ (**15%**)  

    ### รูปแบบข้อมูล (Class Labels)  
    - **MEN**: คลาสที่แทนผู้ชาย  
    - **WOMAN**: คลาสที่แทนผู้หญิง  
    """)

    st.subheader("Data Augmentation เพื่อป้องกัน Overfitting")
    st.write("""
    Data Augmentation ใช้สร้างข้อมูลภาพเพิ่มเติมโดยการแปลงภาพต้นฉบับให้มีความหลากหลายมากขึ้น ช่วยลด Overfitting 
    """)


    st.markdown("""
    **เทคนิคที่ใช้จากโค้ด:**
    - ปรับขนาดค่าพิกเซลของภาพ ให้อยู่ในช่วง [0,1]  (`rescale=1./255`)
    - หมุนภาพได้สูงสุด ±20 องศา (`rotation_range=20`)
    - เลื่อนภาพในแนวแกน X/Y ได้ ±20% (`width_shift_range=0.2`, `height_shift_range=0.2`)
    - พลิกภาพแนวนอน (`horizontal_flip=True`)
    """)

    st.header("2. ทฤษฎีของอัลกอริทึมที่ใช้")
    st.subheader("Convolutional Neural Network (CNN)")
    st.write("""
    CNN เป็น Neural Network ที่ออกแบบมาเพื่อวิเคราะห์ข้อมูลภาพ โดยใช้โครงสร้างหลักดังนี้:
    1. Convolutional Layer - ใช้ฟิลเตอร์เพื่อดึงคุณลักษณะจากภาพ
    2. Pooling Layer - ลดขนาดของข้อมูลแต่ยังคงคุณลักษณะสำคัญ
    3. Fully Connected Layer - ใช้ในการตัดสินใจว่าภาพเป็นเพศใด
    4. Activation Function - ใช้ ReLU ในชั้นซ่อน และ Sigmoid ในชั้นเอาต์พุต
    """)

    st.header("3. ขั้นตอนการพัฒนาโมเดล")
    st.write("""
    1. โหลดและเตรียมข้อมูลจาก Dataset
    2. เพิ่ม Data Augmentation เพื่อเพิ่มจำนวนภาพเทียม
    3. สร้างโครงสร้างโมเดล CNN 
    4. ใช้ Batch Normalization และ Dropout เพื่อเพิ่มประสิทธิภาพของโมเดล
    5. เพิ่ม Data Augmentation เพื่อเพิ่มจำนวนภาพเทียม
    6. ฝึกโมเดลโดยใช้ Adam Optimizer
    7. ใช้ Early Stopping และ ReduceLROnPlateau เพื่อป้องกัน Overfitting
    8. ทดสอบและประเมินผล
    9. บันทึกโมเดลและนำไปใช้งาน
    """)

    st.subheader("Early Stopping และ ReduceLROnPlateau เพื่อป้องกัน Overfitting")
    st.write("""
    - **Early Stopping** หยุดการฝึกโมเดลอัตโนมัติหาก `val_loss` ไม่ลดลงเป็นระยะเวลาที่กำหนด (`patience=5`)
    - **ReduceLROnPlateau** ปรับลดค่า Learning Rate ลงเมื่อ `val_loss` หยุดพัฒนา (`factor=0.5`, `patience=3`, `min_lr=1e-6`)
    """)

    st.header("4. การประเมินผลลัพธ์ (Model Evaluation)")
    st.write("""
    ผลของโมเดลนี้มีการประเมินใน 2 ส่วนหลัก คือ:

    1. **ส่วนการพัฒนา**:
        - ✅ โมเดลทำงานได้ดีระดับหนึ่ง:
            - Training Accuracy: 85%
            - Validation Accuracy: 76%

    2. **ส่วน Test Set**:
        - โหลดข้อมูล Test Set
        - คำนวณค่า Loss และ Accuracy
        - แสดงผล Test Accuracy:
            - ✅ **Test Accuracy (84.18%)** ค่อนข้างดี → โมเดลสามารถใช้งานได้ในระดับหนึ่ง
            - ✅ **Loss (0.3243)** ต่ำ → โมเดลพยากรณ์ได้แม่นยำ ไม่มีความผิดพลาดสูงเกินไป
    """)

    st.header("5. การนำโมเดลไปใช้งาน")
    st.write("""
    - โหลดโมเดลที่ฝึกไว้แล้ว (`gender_classification2_model.h5`)
    - ใช้โมเดลในการทำนายภาพใหม่
    - ทดสอบโมเดลด้วยข้อมูลจากแหล่งอื่นเพื่อดูความแม่นยำในการใช้งานจริง
    """)


if __name__ == "__main__":
    app()
