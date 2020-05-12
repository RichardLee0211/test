import numpy as np
import matplotlib.pyplot as plt
import time

# interactive drawing, got to try it in ipython or other python shell
"""
plt.ion() # interactive mode on
plt.plot([1.6, 2.7])
plt.show()
time.sleep(1)

plt.title("interactive test")
plt.xlabel("index")
time.sleep(1)

ax = plt.gca()
ax.plot([3.1, 2.2])
"""


# plot coutour
"""
x = np.arange(-6, 6, 1)
y = np.arange(-5, 5, 1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2) # broadcast, I guess
# h = plt.contourf(x,y,z)
h = plt.contour(x,y,z)
# plt.legend()
plt.show()
"""
