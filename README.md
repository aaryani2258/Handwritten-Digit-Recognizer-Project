<<<<<<< HEAD
# 🔢 Handwritten Digit Recognizer

## Project Overview

A CNN-based deep learning model that recognizes handwritten digits using the MNIST dataset.

## Dataset Information

MNIST Dataset

- 60,000 training images
- 10,000 testing images
- Digits from 0 to 9

## Technologies Used
=======
# 🔢 Handwritten Digit Recognizer Using CNN

## 📌 Project Overview

The Handwritten Digit Recognizer is a Deep Learning project that uses a Convolutional Neural Network (CNN) to identify handwritten digits from images.

The model is trained using the MNIST dataset, which contains thousands of handwritten digit images. Users can upload digit images through a Streamlit web application and receive instant predictions.

This project demonstrates the application of Computer Vision, Image Processing, and Deep Learning techniques.

---

## 🎯 Objectives

- Recognize handwritten digits accurately.
- Learn image preprocessing techniques.
- Understand Convolutional Neural Networks (CNNs).
- Train and evaluate a deep learning model.
- Deploy the model using Streamlit.

---

## 📂 Dataset Information

### Dataset Name

MNIST Dataset

### Dataset Description

The MNIST dataset contains grayscale handwritten digit images.

- Training Images: 60,000
- Testing Images: 10,000
- Image Size: 28 × 28 pixels
- Classes: 10 (Digits 0–9)

### Sample Classes

```text
0 1 2 3 4 5 6 7 8 9
```

---

## 🛠️ Technologies Used
>>>>>>> 784fd96ede4b9e545f42fd0a92bd483ee3f32162

- Python
- TensorFlow
- Keras
- NumPy
- Streamlit
- Pillow

## Deep Learning Model

Convolutional Neural Network (CNN)

Layers:

- Conv2D
- MaxPooling2D
- Flatten
- Dense

## Accuracy Achieved

Approximately 98%–99%

## Screenshots

### Home Page

![Home](screenshots/homepage.png)

### Prediction

![Prediction](screenshots/prediction.png)

## Installation

```bash
pip install -r requirements.txt
```

## Run

Train:

```bash
python train_model.py
```

Launch App:

```bash
streamlit run app.py
```

## Future Enhancements

- Digit drawing canvas
- Real-time prediction
- Mobile deployment
- Cloud hosting

## Author

B.Aaryani

## Project

Codec Technologies Internship Project
