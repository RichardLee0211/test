## some tests on linalg
import numpy as np
from scipy import linalg
"""
A = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
print(A.dot(linalg.inv(A)))

A = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
# way 1
linalg.inv(A).dot(b) # slow array([[-4. ],
A.dot(linalg.inv(A).dot(b)) - b # check
# way 2
np.linalg.solve(A, b) # fast
A.dot(np.linalg.solve(A, b)) - b # check
"""

import random
import matplotlib.pyplot as plt
# a good way to plot histogram
N = 10000
rlist = [random.random() for _ in range(N)] # a more python way
# rlist= []
# for i in range(N):
    # rlist.append(random.random())
hist, bin_edges = np.histogram(rlist, bins=100)
y = hist
x = (bin_edges[:-1] + bin_edges[1:]) * .5
plt.bar(x, y, width=0.005)
plt.show()
