from scipy.stats import binom
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import datetime

# plot binom distribution
"""
fig, ax = plt.subplots(1, 1)
n, p = 125, 0.4
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')

x = np.arange(binom.ppf(0.01, n, p),
        binom.ppf(0.99, n, p))
ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
# ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
plt.show()
"""

# random variable sampling
"""
SEED = datetime.datetime.now().microsecond
N = 5000
Y = norm.rvs(size=N, random_state=SEED)
# hist = np.histogram(Y)
plt.hist(Y, bins=np.linspace(-5, 5, 100))
plt.show()
"""

# plot pdf and cdf
"""
xlim = 5
n_sample = 10000
X = np.linspace(-xlim, xlim, n_sample)
# Y = norm.pdf(X)
Y = norm.cdf(X)
plt.plot(X, Y)
plt.show()
"""

# plot binom pmf
"""
n, p = 10, 0.75 # 0.25
rv = binom(n, p)
x = np.arange(0, n+1)
# plt.plot(x, rv.pmf(x), 'bo', ms=11, label='binom pmf')
plt.bar(x, rv.pmf(x))
plt.show()
"""

# plot poisson pmf
"""
from scipy.stats import poisson
mu = 10 # 1
x = np.linspace(0, 30, 30, dtype=int)
y = poisson.pmf(x, mu)
plt.bar(x, y)
plt.show()
"""


# sums of independent random variables have an approximately Gaussian distribution
"""
import random
n_random_per_block = 20
n_block = 5000
random.seed(1357973)
sums = np.zeros(n_block)
for i in range(n_block):
    for j in range(n_random_per_block):
        sums[i] += (1 - 2*random.random())

x, y = np.histogram(sums, bins=np.linspace(-5, 5, 100), density=True)
plt.scatter(y[:-1], x)
# normal distribution
from scipy.stats import norm
x = np.linspace(-5, 5, 100)
# mu_2 = 1.0 / math.sqrt(n_block)
y = norm.pdf(x, 0, 2.5)
plt.plot(x, y)
plt.show()
"""

# plot Norm, student T and laplace's pdf
"""
from scipy.stats import norm
from scipy.stats import t
from scipy.stats import laplace
x = np.linspace(-5, 5, 500)
y_norm = norm.pdf(x, 0, 1) # mean(\mu) various(\sigma^2)
y_t = t.pdf(x, 1) # degree of freedom
y_laplace = laplace.pdf(x)
plt.subplot(211)
plt.plot(x, y_t, "b-", label="student t(1)")
plt.plot(x, y_norm, "g-", label="Norm(0, 1)")
plt.plot(x, y_laplace, "c-", label="laplace()")
plt.legend(frameon=False)
plt.subplot(212)
plt.plot(x, norm.logpdf(x, 0, 1), label="norm.logpdf(0, 1)")
plt.plot(x, t.logpdf(x, 1), label="t.logpdf(1)")
plt.plot(x, laplace.logpdf(x), label="laplace.logpdf()")
plt.legend(frameon=False)
plt.show()
"""

# find the favoriate line style
"""
x = np.linspace(0, 12, 5000)
y = np.sin(x)
# I would say default color is better than any preset color in "bgmrckyw"
plt.plot(x, y)
plt.plot(x, y+0.1)
plt.plot(x, y+0.2)
plt.plot(x, y+0.3)
# plt.plot(x, y, 'b-', label="blue")
# plt.plot(x, y+0.1, 'g-', label="green")
# plt.plot(x, y+0.2, 'm-', label="magenta")
# plt.plot(x, y+0.2, 'r-', label="blue") # not like red, except extrem important
# plt.plot(x, y+0.5, 'c-', label="cyan")
# plt.plot(x, y+0.3, 'k-', label="black")
# plt.plot(x, y+0.4, 'y-', label="yellow")
# plt.plot(x, y+0.3, 'w-', label="white")
# plt.legend()
plt.show()
"""

# plot bivariate norm distribution
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from scipy.stats import norm
"""
x = np.linspace(0, 5, 100, endpoint=False)
y = multivariate_normal.pdf(x, mean=2.5, cov=0.5)
y_norm = norm.pdf(x, 2.5, 0.5)
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(x, y, label="multivariate_normal(mean=2.5, cov=0.5)")
ax.plot(x, y_norm, label="norm(mean=2.5, var=0.5)")
plt.legend()
plt.show()

import matplotlib.cm as cm
BONDARY = 3
dx=dy = 0.01
x, y = np.mgrid[-BONDARY:BONDARY:.01, -BONDARY:BONDARY:.01]
pos = np.dstack((x, y)) # this is interesting function, stack
rv = multivariate_normal([0.5, -0.2], [[2.0, 0.3], [0.3, 0.5]]) # mean vectors and cov
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
# ax2.contourf(x, y, rv.pdf(pos))
# ax2.plot_surface(x, y, rv.pdf(pos), cmap = cm.hot)
ax2.plot_surface(x, y, rv.pdf(pos), cmap = cm.Greys)
plt.show()
"""

# This import registers the 3D projection, but is otherwise unused.
# from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

from matplotlib import cm
"""
# contour plots, but it seems that plot_surface is better for this formula
# it seems to be a un-natural way to combine 2D plot with 3D plot
x = np.linspace(0,10,51)
y = np.linspace(0,8,41)
(X,Y) = np.meshgrid(x,y)
a = np.exp(-((X-2.5)**2 + (Y-4)**2)/4) - np.exp(-((X-7.5)**2 + (Y-4)**2)/4)
#### contour plot
c = plt.contour(X,Y,a)
l = plt.clabel(c)
#### contour filled
# c = plt.contourf(x,y,a,np.linspace(-1,1,11))
# b = plt.colorbar(c, orientation='vertical')
# ax = plt.axis([0,10,0,8])
#### 3d surface plot
# ax = plt.gca(projection='3d')
# surp = ax.plot_surface(X, Y, a, cmap=cm.coolwarm)
# plt.colorbar(surp)
lx = plt.xlabel("x")
ly = plt.ylabel("y")
plt.show()
"""

# a good example of surface plot
# from: https://scipython.com/book/chapter-7-matplotlib/examples/simple-surface-plots/
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

L, n = 2, 400
x = np.linspace(-L, L, n)
y = x.copy()
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2))

fig, ax = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': '3d'})
ax[0,0].plot_wireframe(X, Y, Z, rstride=40, cstride=40)
ax[0,1].plot_surface(X, Y, Z, rstride=40, cstride=40, color='m')
ax[1,0].plot_surface(X, Y, Z, rstride=12, cstride=12, color='m')
ax[1,1].plot_surface(X, Y, Z, rstride=20, cstride=20, cmap=cm.hot)
for axes in ax.flatten():
    axes.set_xticks([-2, -1, 0, 1, 2])
    axes.set_yticks([-2, -1, 0, 1, 2])
    axes.set_zticks([0, 0.5, 1])
fig.tight_layout()
plt.show()
"""
