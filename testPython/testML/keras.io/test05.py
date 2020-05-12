# Sequence classification with 1D convolutions
# TODO: modify this

import random as rn
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding, Reshape
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D


""" baby LCG """
A = 68
B = 3
M = 54132
x = 51
def foo():
    global A, B, M, x
    x_tmp = (A*x+B) % M
    x = x_tmp
    return x_tmp % 100


seq_length = 64
n_CATA = 100
n_sample = 128
n_test_sample = 128

def generate_seq():
    X = []
    y = []
    for _ in range(seq_length):
        X.append(foo())
    y.append(foo())
    return np.array(X), np.array(y)

X_train = []
y_train = []
X_test = []
y_test = []

for _ in range(n_sample):
    X, y = generate_seq()
    X_train.append(X)
    y_train.append(y)

for _ in range(n_test_sample):
    X, y = generate_seq()
    X_test.append(X)
    y_test.append(y)

X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)

input_shape = seq_length*1

X_train = X_train.reshape(X_train.shape[0], input_shape)
y_train = keras.utils.to_categorical(y_train, num_classes=n_CATA)

X_test = X_test.reshape(X_test.shape[0], input_shape)
y_test = keras.utils.to_categorical(y_test, num_classes=n_CATA)

print(f"X_train.shape: {X_train.shape}")
print(f"y_train.shape: {y_train.shape}")

print(f"X_test.shape: {X_test.shape}")
print(f"y_test.shape: {y_test.shape}")

model = Sequential()
# model.add(Conv1D(64, 3, activation='relu', input_shape=(seq_length, n_CATA)))
model.add(Reshape((seq_length, 1), input_shape=(input_shape,)))
model.add(Conv1D(64, 3, activation='relu', input_shape=(seq_length, 1)))
model.add(Conv1D(64, 3, activation='relu'))
model.add(MaxPooling1D(3))
model.add(Conv1D(128, 3, activation='relu'))
model.add(Conv1D(128, 3, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(n_CATA, activation='softmax'))

model.compile(loss='categorical_crossentropy',
                    optimizer='rmsprop',
                    metrics=['accuracy'])

print(model.summary())


"""
"""
model.fit(X_train, y_train,
        validation_data = (X_test, y_test),
        batch_size=16, epochs=100)
# score = model.evaluate(x_test, y_test, batch_size=16)

"""
model = Sequential()
model.add(Conv1D(64, 3, activation='relu', input_shape=(seq_length, 100)))
model.add(Conv1D(64, 3, activation='relu'))
model.add(MaxPooling1D(3))
model.add(Conv1D(128, 3, activation='relu'))
model.add(Conv1D(128, 3, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
                    optimizer='rmsprop',
                    metrics=['accuracy'])
"""
