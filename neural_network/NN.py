import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import base64
from io import BytesIO
import os

file_path = "gender_classification2_model.tflite"

if os.path.exists(file_path):
    file_size = os.path.getsize(file_path) / (1024 * 1024)  # แปลงเป็น MB
    print(f"📏 ขนาดไฟล์ .tflite: {file_size:.2f} MB")
else:
    print("❌ ไม่พบไฟล์ .tflite")



# โหลดโมเดล .tflite
interpreter = tf.lite.Interpreter(model_path=file_path)
interpreter.allocate_tensors()

# ดึงรายละเอียดของ input / output tensor
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess_image(image):
    """ แปลงภาพให้เป็นรูปแบบที่เหมาะกับโมเดล """
    img_resized = cv2.resize(image, (128, 128))  # ปรับขนาดเป็น 128x128
    img_resized = img_resized.astype(np.float32) / 255.0  # ปรับค่าสีเป็น 0-1
    img_resized = np.expand_dims(img_resized, axis=0)  # เพิ่ม batch dimension
    return img_resized

def predict_gender(image):
    """ ใช้โมเดล .tflite ในการพยากรณ์เพศ """
    input_data = preprocess_image(image)
    
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()  # รันโมเดล
    
    output_data = interpreter.get_tensor(output_details[0]['index'])
    confidence = float(output_data[0][0]) * 100  # ค่าความมั่นใจ
    
    gender = "WOMAN" if confidence > 50 else "MAN"
    return gender, confidence

def app():
    st.markdown("<h1 style='text-align: center;'>Gender Classification</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Upload an image and classify gender</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        image = np.array(image)

        # แสดงภาพ
        buffered = BytesIO()
        img_pil = Image.fromarray(image)
        img_pil.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

        st.markdown(
            f"<div style='text-align: center;'><img src='data:image/jpeg;base64,{img_base64}' width='350'></div>",
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)
        # ใช้ HTML และ CSS เพื่อจัดปุ่มให้อยู่ตรงกลาง
        st.markdown(
            """
            <style>
            .stButton>button {
                display: block;
                margin: 0 auto;
                text-align: center;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        if st.button("Predict Gender"):
            gender, confidence = predict_gender(image)
            
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <h3>Prediction: <strong>{gender}</strong></h3>
                    <p>Confidence Score: {confidence:.2f}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )


