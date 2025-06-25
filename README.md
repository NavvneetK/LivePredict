# LivePredict – Real-Time Age & Gender Prediction from Images

LivePredict is a deep learning-based web app that predicts **age and gender** from user-uploaded images using a fine-tuned TensorFlow model. Built with **Streamlit**, it offers a fast and interactive frontend experience.

## 🔍 Features

- Upload an image and get instant predictions of age and gender.
- Clean UI using Streamlit.
- Deep learning model trained using TensorFlow & Keras.
- Face detection and bounding box visualization.
- Easily deployable as a web app.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Model:** TensorFlow, OpenCV
- **Deployment:** Streamlit Cloud / Local

## 📦 Installation

```bash
git clone https://github.com/NavvneetK/LivePredict.git
cd LivePredict
pip install -r requirements.txt
streamlit run app.py
```


## 🧠 Model Information

This project uses a deep learning model named **`gender_age_model.h5`**, built using **Transfer Learning** on **MobileNet** architecture with **Keras** and **TensorFlow backend**.

### 🔍 Model Purpose
- **Task 1:** Predict **Gender** → Male / Female (Binary classification)
- **Task 2:** Predict **Age** → Exact numeric value (Regression)

### 🧬 Architecture Details
- **Base Model:** `MobileNetV2` (pretrained on ImageNet, frozen base)
- **Custom Top Layers:**
  - Global Average Pooling
  - Dense layers for classification (gender) and regression (age)
- **Input Shape:** 100x100 RGB face images
- **Loss Function:**
  - `binary_crossentropy` for gender classification
  - `mean_absolute_error (mae)` for age regression
- **Optimizer:** Adam
- **Training Dataset:** UTK dataset with labeled face images (Age + Gender)


---

## ✨ Features

- Upload face images and get **live age and gender prediction**
- Uses **Transfer Learning** with **MobileNetV2** for fast and accurate inference
- Lightweight frontend built using **Streamlit**
- Easily deployable on **Streamlit Cloud**

---

## 🚀 Future Enhancements

- Enable **real-time webcam-based prediction**
- Add drag-and-drop or mobile camera support
- Enhance model accuracy with larger datasets
- Reduce model size with quantization/pruning

---

## 🤝 Contributing

Pull requests are welcome.  
For major changes, please open an issue first to discuss what you would like to change.

---
