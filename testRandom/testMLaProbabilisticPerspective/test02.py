## some test on linalg
import numpy as np
from scipy import linalg
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
