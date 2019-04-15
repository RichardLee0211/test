
d code
Ch02 probability
--------------------------------------------------------------------------------
Probability theory is nothing but common sense reduced to calculation. — Pierre Laplace, 1812

TODO: how to draw these pics in python, page.33

find some book accordint to this wiki page
https://en.wikipedia.org/wiki/Categorical_distribution

distinguish classical ways of PRNGs and prediction


others
--------------------------------------------------------------------------------
in python, I wouldn't worry about understand-lying data structure of variable
preview Go back, <Cmd+[> would be handy when jumping around pages.

### reading scipy doc
#### reading 4.1.7 Fourier Transforms in scipy.fftpack reference
from scipy.fftpack import fft
I can't help it, got to code it
I really know a little about Fourier Transform and how to use it

#### reading 4.1.9 Linear Algebra(scipy.linalg)
```python
import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
linalg.inv(A)
b = np.array([[5,6]]) # 2D array
A*b # not matrix multiplication!
A.dot(b.T) # matrix multiplication
b = np.array([5,6]) # 1D array

```

```shell
>>> b = np.array([5,6]) #1D array >>> b
array([5, 6])
>>> b.T #not matrix transpose! array([5, 6])
>>> A.dot(b) # does not matter for multiplication array([17, 39])
```
Yeah, I know little about matrix

#### reading 4.1.13 statistics (scipy.stats)
TODO_2: what's Hazard Function for ?? what's skewness for ??

pmf, probability mass function, p in math notation
cdf, cumulative distribution function. F in math notation
ppf, percent point function, G in math notation

\mu, mean
\mu_2, variance
\gamma_1, skewness
\gamma_2, (Fisher) kurtosis

moment generating function, never heared of

so many continuous Statical distributions, over 80
and God know how to fit them into practical cases

#### kernel Density Estimation(KDE)

### reading a little matplotlib by the way
from: https://matplotlib.org/tutorials/introductory/usage.html
a recommend way to plot
```python
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
```

about plt.subplots()
from: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html
```python
    #First create some toy data:
    x = np.linspace(0, 2*np.pi, 400)
    y = np.sin(x**2)

    #Creates just a figure and only one subplot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Simple plot')

    #Creates two subplots and unpacks the output array immediately
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.plot(x, y)
    ax1.set_title('Sharing Y axis')
    ax2.scatter(x, y)

    #Creates four polar axes, and accesses them through the returned array
    fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
    axes[0, 0].plot(x, y)
    axes[1, 1].scatter(x, y)
```

plt.subplots() return figure and axes
plt.subplot() set current axes
```python
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]

    plt.figure(1, figsize=(9, 3))

    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()
```

I think I find a way to plot auto-correlation
plt.acorr(x)
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.acorr.html
plt.gca() return current axes
plt.gcf() return current figure

write code for a picture may not be so pleasant, but write code for visualization
of data would be cool

a generate example
```python
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()
```

annotating text
```python
    x = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                              )

    plt.ylim(-2, 2)
    plt.show()
```

Logarithmic and other nonlinear axes, helpful when data spans many orders of
magnitude. Saved for the future

subplot example
```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(19680801)
    data = np.random.randn(2, 100)

    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    axs[0, 0].hist(data[0])
    axs[1, 0].scatter(data[0], data[1])
    axs[0, 1].plot(data[0], data[1])
    axs[1, 1].hist2d(data[0], data[1])

    plt.show()
```

TODO: to master
https://matplotlib.org/gallery/images_contours_and_fields/pcolormesh_levels.html
this is one way to observe the 3D data
