import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# Load model
@st.cache_resource
def load_my_model():
    return load_model("gender_age_model.keras")

model = load_my_model()

# Prediction function
def predict(image):
    image = image.resize((100, 100))
    img = np.array(image) / 255.0
    img = np.expand_dims(img, axis=0)

    gender_pred, age_pred = model.predict(img)
    gender = "Male" if gender_pred[0][0] > 0.5 else "Female"
    age = int(age_pred[0][0])

    return gender, age

# UI
st.title("🧠 Age & Gender Prediction from Image")
st.write("Upload a face image, and the model will predict age & gender! Image type=[jpg, jpeg, png]")

uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        gender, age = predict(image)
        st.success(f"👤 Gender: {gender}")
        st.success(f"🎂 Age: {age}")
