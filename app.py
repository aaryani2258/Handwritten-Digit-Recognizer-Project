import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

st.set_page_config(
    page_title="Digit Recognizer",
    page_icon="🔢"
)

model = load_model("models/digit_model.h5")

st.title("🔢 Handwritten Digit Recognizer")

uploaded_file = st.file_uploader(
    "Upload Digit Image",
    type=["png","jpg","jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert('L')

    st.image(image, caption="Uploaded Image")

    image = image.resize((28,28))

    img = np.array(image)

    img = 255 - img

    img = img / 255.0

    img = img.reshape(1,28,28,1)

    prediction = model.predict(img)

    digit = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    st.success(
         f"Predicted Digit: {digit} ({confidence:.2f}% confidence)"
    )

