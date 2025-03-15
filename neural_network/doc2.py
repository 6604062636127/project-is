import streamlit as st

def app():
    
    st.title("แนวทางการพัฒนา Neural Network สำหรับแยกเพศจากภาพ")

    st.header("1. การเตรียมข้อมูล (Data Preparation)")
    st.write("""
    - ดาวน์โหลด Dataset จาก Kaggle https://www.kaggle.com/datasets/humairmunir/gender-recognizer
    - จัดการและแบ่งข้อมูลเป็น Training 70%, Validation 15%, และ Test 15%
    - โครงสร้างไฟล์ข้อมูลมีสองคลาส: MEN และ WOMAN
    - ใช้ Data Augmentation เพื่อเพิ่มความหลากหลายของข้อมูล
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
