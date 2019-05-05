
# for OMP: Error #15
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import numpy as np
import random
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense

LENGTH = 4
UP_LIM = 32
DOWN_LIM = 0
SEED = 0
TRAIN_SAMPLE = 128
TEST_SAMPLE = 100

EPOCHS = 50

# a, b, num = 2, 0, 1
a = 2
b = 0
num = 1
def test_random():
    global num, a, b
    num = (a*num + b) / UP_LIM
    return num

if __name__ == "__main__":
    random.seed(SEED)

    print("generate data")
    """training data"""
    X_train = []
    y_train = []
    for _ in range(TRAIN_SAMPLE):
        seq = [random.randint(DOWN_LIM, UP_LIM) for _ in range(LENGTH)]
        X_train.append(seq[:-1])
        y_tmp = np.zeros(UP_LIM-DOWN_LIM+1)
        index = seq[-1]
        y_tmp[index] = 1
        y_train.append(y_tmp)
    # print(X)
    X_train = np.array(X_train)
    y_train = np.array(y_train)

    """test data"""
    X_test = []
    y_test = []
    for _ in range(TEST_SAMPLE):
        seq = [random.randint(DOWN_LIM, UP_LIM) for _ in range(LENGTH)]
        X_test.append(seq[:-1])
        y_tmp = np.zeros(UP_LIM-DOWN_LIM+1)
        index = seq[-1]
        y_tmp[index] = 1
        y_test.append(y_tmp)

    X_test = np.array(X_test)
    y_test = np.array(y_test)
    print("END of generate data")

    """ model """
    model = Sequential()
    model.add(  Dense(1024, input_shape=(LENGTH-1, ), activation='relu'))
    model.add(  Dense(1024, activation='relu'))
    # model.add(LSTM(50, stateful=True))
    model.add(  Dense(UP_LIM-DOWN_LIM+1, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])


    """ fit """
    # batch_size default 32
    model.fit(X_train, y_train,
            epochs = EPOCHS,
            validation_data=(X_test, y_test)
            )

    """
    seq = [random.randint(0, 32) for _ in range(LENGTH)]
    X_test = seq[:-1]
    y_test = seq[-1]
    model.evaluate(x_test, y_test)
    """
