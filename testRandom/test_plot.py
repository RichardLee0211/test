import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2],[1,2])
# plt.show()
x = np.arange(0, 25, 0.01)
y = np.sin(x)
plt.plot(x, y)
# plt.show()
# y_2 = sin(x) ** 2
"""
y_2 = np.float_power(y, 2)
plt.plot(x, y_2)
plt.show()
"""
"""
# this is a test
y_3 = np.float_power(np.sin(x),2)+np.float_power(np.cos(x), 2)
plt.plot(x, y_3)
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
