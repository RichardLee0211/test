#! /Users/richardlee/python_tutorial_env/bin/python

# %matplotlib inline
import  matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

boston_dataset = datasets.load_boston()
X_full = boston_dataset.data
Y = boston_dataset.target
# print X_full.shape # python2 syntax
# print Y.shape
# print (X_full.shape)
# print (Y.shape)
# print (boston_dataset.DESCR)
print (boston_dataset.data)
print (boston_dataset.feature_names)

# selector = SelectKBest(f_regression, k=1)
# selector.fit(X_full, Y)
# X = X_full[:, selector.get_support()]
# print (X.shape)

# plt.scatter(X, Y, color='black')
# plt.show()

# regressor = LinearRegression(normalize=True)
# regressor.fit(X, Y)
# plt.scatter(X, Y, color='black')
# plt.plot(X, regressor.predict(X), color='blue', linewidth=3)
# plt.show()

# regressor = SVR()
# regressor.fit(X, Y)
# plt.scatter(X, Y, color='black')
# plt.scatter(X, regressor.predict(X), color='blue', linewidth=3)
# plt.show()

# regressor = RandomForestRegressor()
# regressor.fit(X, Y)
# plt.scatter(X, Y, color='black');
# plt.scatter(X, regressor.predict(X), color='blue', linewidth=3)
# plt.show()
