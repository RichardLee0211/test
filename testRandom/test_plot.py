import matplotlib.pyplot as plt
import numpy as np

"""
# plt.plot([1,2],[1,2])
# plt.show()
x = np.arange(0, 25, 0.01)
y = np.sin(x)
plt.plot(x, y)
# plt.show()
# y_2 = sin(x) ** 2
"""

x = np.arange(0, 10, 1)
# y = np.sin(x)
y = np.array([
    0.140625, 0.84375, 0.882812, 0.921875, 0.882812,
    0.90625, 0.882812, 0.914062, 0.875, 0.90625])
y_loss = np.array([
3.67079 , 0.492122, 0.421595, 0.307726, 0.392948,
0.371461, 0.378425, 0.338605, 0.379697, 0.444303    ])

"""
Iteration 0     | Loss = 3.67079    | Accuracy = 0.140625
Iteration 100   | Loss = 0.492122   | Accuracy = 0.84375
Iteration 200   | Loss = 0.421595   | Accuracy = 0.882812
Iteration 300   | Loss = 0.307726   | Accuracy = 0.921875
Iteration 400   | Loss = 0.392948   | Accuracy = 0.882812
Iteration 500   | Loss = 0.371461   | Accuracy = 0.90625
Iteration 600   | Loss = 0.378425   | Accuracy = 0.882812
Iteration 700   | Loss = 0.338605   | Accuracy = 0.914062
Iteration 800   | Loss = 0.379697   | Accuracy = 0.875
Iteration 900   | Loss = 0.444303   | Accuracy = 0.90625]
"""
plt.plot(x, y)
plt.plot(x, y_loss/3.0)
plt.title("Accu and Loss")
plt.grid()
plt.show()

model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(1024, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])


plt.plot(x, y_2)
plt.show()
"""
# this is a test
y_3 = np.float_power(np.sin(x),2)+np.float_power(np.cos(x), 2)
plt.plot(x, y_3)
"""

model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])= np.float_power(y, 2)


"""
y_5 = np.cos(x)
plt.plot(x, y_5)
y_4 = np.sin(x)+np.cos(x)
plt.plot(x, y_4)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())
plt.show()
"""
