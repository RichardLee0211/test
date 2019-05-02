# from: https://scikit-learn.org/stable/tutorial/statistical_inference/index.html

import numpy as np
from sklearn import datasets
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
"""
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
print(np.unique(iris_y)) # output array([0, 1, 2])
"""

# Split iris data in train and test data
# A random permutation, to split the data randomly
"""
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
"""

## diabete dataset
#-------------------------------------------------------------------------------
"""
diabetes = datasets.load_diabetes()
diabetes_X_train = diabetes.data[:-20]
diabetes_X_test  = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test  = diabetes.target[-20:]
"""

# Create and fit a nearest-neighbor classifier
#-------------------------------------------------------------------------------
"""
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)

print(knn.predict(iris_X_test))
print(iris_y_test)
"""


## linear model
#-------------------------------------------------------------------------------
"""
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)

print(regr.coef_)

# The mean square error
MSE = np.mean((regr.predict(diabetes_X_test) - diabetes_y_test)**2)
print(f"MSE: {MSE}")

# Explained variance score: 1 is perfect prediction
# and 0 means that there is no linear relationship
# between X and y.
regr.score(diabetes_X_test, diabetes_y_test)
"""

## Shrinkage
#-------------------------------------------------------------------------------
X = np.c_[ .5, 1].T
y = [.5, 1]
test = np.c_[ 0, 2].T

"""
regr = linear_model.LinearRegression()
plt.figure()
np.random.seed(0)
for _ in range(6):
    this_X = .1 * np.random.normal(size=(2, 1)) + X
    regr.fit(this_X, y)
    plt.plot(test, regr.predict(test))
    plt.scatter(this_X, y, s=3)
plt.show()
"""

## Ridge
"""
regr = linear_model.Ridge(alpha=.1)
plt.figure()
np.random.seed(0)
for _ in range(6):
    this_X = .1 * np.random.normal(size=(2, 1)) + X
    regr.fit(this_X, y)
    plt.plot(test, regr.predict(test))
    plt.scatter(this_X, y, s=3)
plt.show()
"""

## classification
#-------------------------------------------------------------------------------
log = linear_model.LogisticRegression(solver='lbfgs', C=1e5,
                                    multi_class='multinomial')
log.fit(iris_X_train, iris_y_train)

## SVM
#-------------------------------------------------------------------------------
from sklearn import svm
svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)

# polynomial
# svc = svm.SVC(kernel='poly', degree=3)

# gamma: inverse of size of radial kernel
# svc = svm.SVC(kernel='rbf')
