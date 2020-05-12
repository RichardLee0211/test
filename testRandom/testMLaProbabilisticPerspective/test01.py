import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import random

# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
noisy = []
for i in range(N):
    noisy.append((1 - 2*random.random()))

# TODO: broadcast .2 * noisy
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x) + 2 * noisy
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x) # + noisy
y = noisy
"""
"""
plt.plot(x, y)
plt.show()

yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

plt.scatter(yf.real, yf.imag)
plt.show()
"""
"""

"""
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
# plt.plot(xf, np.abs(yf[0:N//2]))
plt.grid()
plt.show()
# this would show a peak at 50 and 80
"""
