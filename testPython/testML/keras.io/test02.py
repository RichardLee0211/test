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

# this is stanadard LCG
"""
A = 16807
B = 0
M = 2147483647
"""

# baby one, but actually work good
"""
A = 68
B = 3
M = 54132
"""

A = 68
B = 0
M = 4328

x = 51
def foo():
    global A, B, M, x
    x_tmp = (A*x+B) % M
    x = x_tmp
    return x_tmp

def generate_sequence_100(n_sample, n_feature):
    ret = []
    for _ in range(n_sample):
        tmp = [ foo()  for _ in range(n_feature)]
        ret.append(np.array(tmp)%100)
    return np.array(ret)

def generate_sequence_unlimit(n_sample, n_feature):
    ret = []
    for _ in range(n_sample):
        tmp = [ foo() for _ in range(n_feature)]
        ret.append(tmp)
    return np.array(ret)


ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

data = generate_sequence_unlimit(400, 1)
# data = data.reshape(-1, 1)
data2 = generate_sequence_100(400, 1)
# data2 = data.reshape(-1, 1)

ax1.plot(data)
ax1.scatter(np.arange(0, len(data)), data)

ax2.plot(data2)
ax2.scatter(np.arange(0, len(data2)), data2)
# plt.imshow(data, cmap=plt.cm.binary)
# ax1.title(f"{A}*x+{B} mod {M}")
plt.show()

"""
INPUT_DIM = 20
n_CATA = 100
n_epochs = 40
data = generate_sequence(10000, INPUT_DIM+1)
x_train = data[:, 0:-1]
y_train = data[:, -1]
y_train = keras.utils.to_categorical(y_train, num_classes=n_CATA)

data = generate_sequence(100, INPUT_DIM+1)
x_test = data[:, 0:-1]
y_test = data[:, -1]
y_test = keras.utils.to_categorical(y_test, num_classes=n_CATA)
"""


# Generate dummy data
"""
np.random.seed(0)
train = np.random.randint(10, size=(1000, 21))
x_train = train[:, 0:-1]
y_train = keras.utils.to_categorical(train[:, -1], num_classes=10)

test = np.random.randint(10, size=(100, 21))
x_test = test[:, 0:-1]
y_test = keras.utils.to_categorical(test[:, -1], num_classes=10)

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
"""
