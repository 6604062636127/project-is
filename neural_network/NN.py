import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import base64
from io import BytesIO
import os
import gdown

url = "https://drive.google.com/uc?export=download&id=1h3r-DOL6OgZlgc36csbrenXXW3V-eDK4"
model_path = "gender_classification2_model.h5"

try:
    model = load_model(model_path)
    st.write("โมเดลถูกโหลดเรียบร้อยแล้ว!")
except:
    st.write("ไม่พบโมเดลในเครื่อง กำลังดาวน์โหลด...")
    gdown.download(url, model_path, quiet=False)
    model = load_model(model_path)
    st.write("โมเดลถูกโหลดเรียบร้อยแล้ว!")

def app():
    st.markdown(
    "<h1 style='text-align: center;'>Gender Classification</h1>",
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .centered { text-align: center; }
        .stButton>button { display: block; margin: 0 auto; }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h3 class="centered">Upload an image and classify gender</h3>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        image = image.convert("RGB")
        image = np.array(image)

        buffered = BytesIO()
        img_pil = Image.fromarray(image)
        img_pil.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{img_base64}" width="350">
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        if st.button("Predict Gender"):
            img_resized = cv2.resize(image, (128, 128))
            img_resized = img_resized / 255.0
            img_resized = np.expand_dims(img_resized, axis=0)

            predictions = model.predict(img_resized)
            confidence = float(predictions[0][0]) * 100

            gender = "WOMAN" if confidence > 50 else "MAN"

            st.markdown(
                f"""
                <div class="centered">
                    <h3>Prediction: <strong>{gender}</strong></h3>
                    <p>Confidence Score: {confidence:.2f}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )
