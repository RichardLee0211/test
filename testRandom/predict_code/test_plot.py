import numpy as np
import matplotlib.pyplot as plt

A = 3
B = 0
M = 1000

A_2 = 4
B_2 = 0
M = 1000


def foo(x):
    return (x*A+B) % M

def foo_2(x):
    return (x*A_2+B) % M

"""
x = np.arange(0, 1000, 0.1)
y = foo(x)
y_2 = foo_2(x)
plt.plot(x, y)
plt.plot(x, y_2)
"""

SEED_3 = 5
A_3 = 16807
B_3 = 0
M_3 = 2147483647
N = 500

def foo_3(x):
    return (x*A_3+B_3) % M_3

x_1 = 3
x_2 = 43
M = 10000000

def foo_4():
    global x_1
    global x_2
    x_2_tmp = (x_1 * x_2) % M
    x_1 = x_2
    x_2 =  x_2_tmp
    return x_2 % 100

# main
#-------------------------------------------------------------------------------
"""
x = np.arange(0, N, 1)
y = [SEED_3]
for _ in range(N-1):
    y.append(foo_3(y[-1]))
"""
x = np.arange(0, N, 1)
y = []
for _ in range(N):
    y.append(foo_4())

y = np.array(y)
plt.scatter(x, y)
plt.plot(x, y)
plt.grid(True)
# plt.title(f"LCG: {A_3}*x + {B_3} mod {M_3}")
plt.title("GG PRNG")
plt.show()
