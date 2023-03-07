import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from utils import reader

def generate(name: str, path: str, size: int):
    mnist = tf.keras.datasets.mnist

    y_train, x_train = reader.getInput(path, ',')

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(size, size)))
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

    model.save(name)

def test(name: str, path: str):
    mnist = tf.keras.datasets.mnist

    y_test, x_test = reader.getInput(path, ',')

    model = tf.keras.models.load_model(name)

    loss, accuracy = model.evaluate(x_test, y_test)

    print(f"Loss: {loss}")
    print(f"Accuracy: {accuracy}")

def predict(name: str, path: str):
    model = tf.keras.models.load_model(name)

    image_number = 0
    while os.path.isfile(f"{path}/digit{image_number}.png"):
        try:
            img = cv2.imread(f"{path}/digit{image_number}.png")[:,:,0]
            img = np.invert(np.array([img]))
            prediction = model.predict(img)
            print(f"This digit is probably a {np.argmax(prediction)}")
            plt.imshow(img[0], cmap=plt.cm.binary)
            plt.show()
        except:
            print('Error!')
        finally:
            image_number += 1