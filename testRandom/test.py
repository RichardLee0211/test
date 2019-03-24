#!python3
import numpy as np
import matplotlib.pyplot as plt
import random

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step =  1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk)
plt.show()
