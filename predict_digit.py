from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('models/digit_model.h5')

img_path = input("Enter image path: ")

img = Image.open(img_path).convert('L')
img = img.resize((28,28))

img = np.array(img)

img = 255 - img

img = img / 255.0

img = img.reshape(1,28,28,1)

prediction = model.predict(img)

digit = np.argmax(prediction)

print("Predicted Digit:", digit)