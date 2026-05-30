from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
import numpy as np

model = load_model("models/digit_model.h5")

(_, _), (X_test, y_test) = mnist.load_data()

X_test = X_test / 255.0
X_test = X_test.reshape(-1, 28, 28, 1)

prediction = model.predict(X_test[:10])

for i in range(10):
    print(
        "Actual:",
        y_test[i],
        "Predicted:",
        np.argmax(prediction[i])
    )