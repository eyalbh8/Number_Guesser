from os import environ 
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
from random import randrange



(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_test = X_test/255

environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

with tf.device("/cpu:0"):
    Guesser_model = load_model('Number_guesser_model.h5')

def Number_prediction(model, index):
    guessed_number = np.argmax(model.predict(X_test[index].reshape(1,28,28)))

    print(f"The number is actually: {y_test[index]}")
    print(f"The model predicted: {guessed_number}")

    plt.imshow(X_test[index].reshape(28,28))
    plt.show()

while True:
    random_number = randrange(0,10000)
    Number_prediction(Guesser_model, random_number)