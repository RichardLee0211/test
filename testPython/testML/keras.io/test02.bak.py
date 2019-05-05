# multilayer perceptron(MLP) for multi-class softmax classification

# for OMP: Error #15
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np
import matplotlib.pyplot as plt

A = 68
B = 3
M = 54132

x = 51
def foo():
    global A, B, M, x
    x_tmp = (A*x+B) % M
    x = x_tmp
    return x_tmp % 100

def generate_sequence(n_sample, n_feature):
    ret = []
    for _ in range(n_sample):
        tmp = [ foo() for _ in range(n_feature)]
        ret.append(tmp)
    return np.array(ret)


"""
data = generate_sequence(400, 1)
data = data.reshape(-1, 1)
plt.plot(data)
plt.scatter(np.arange(0, len(data)), data)
plt.show()
"""


INPUT_DIM = 20
n_CATA = 100
n_epochs = 40
data = generate_sequence(1000, INPUT_DIM+1)
x_train = data[:, 0:-1]
y_train = data[:, -1]
y_train = keras.utils.to_categorical(y_train, num_classes=n_CATA)

data = generate_sequence(100, INPUT_DIM+1)
x_test = data[:, 0:-1]
y_test = data[:, -1]
y_test = keras.utils.to_categorical(y_test, num_classes=n_CATA)


# Generate dummy data
"""
np.random.seed(0)
train = np.random.randint(10, size=(1000, 21))
x_train = train[:, 0:-1]
y_train = keras.utils.to_categorical(train[:, -1], num_classes=10)

test = np.random.randint(10, size=(100, 21))
x_test = test[:, 0:-1]
y_test = keras.utils.to_categorical(test[:, -1], num_classes=10)
"""

tf.set_random_seed(1234) # don't really set it steal
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=INPUT_DIM))
# model.add(Dropout(0.9))
model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(n_CATA, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
            optimizer=sgd,
            metrics=['accuracy'])

model.fit(x_train, y_train,
            epochs=n_epochs, batch_size=128,
            validation_data=(x_test, y_test)
            )

# score = model.evaluate(x_test, y_test, batch_size=128)
