import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

# For a single-input model with 10 classes (categorical classification):
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# Generate dummy data
# data = np.random.random((1000, 101))
# labels = np.random.randint(10, size=(1000, 1))
data_n_m = np.random.randint(10, size=(1000, 101))
labels_n = data_n_m[:, -1]
data = data_n_m [:, 0:-1]

test = np.random.randint(10, size=(100, 101))
test_labels = test[:, -1]
test_data = test[:, 0:-1]

# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels_n, num_classes=10)
test_one_hot_labels = keras.utils.to_categorical(test_labels, num_classes=10)

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, one_hot_labels,
        epochs=100, batch_size=32,
        validation_data=(test_data, test_one_hot_labels)
        )
