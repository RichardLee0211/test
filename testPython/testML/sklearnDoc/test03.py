import numpy as np
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
y= iris.target
iris_X = iris.data[y!=0, :2]
iris_y = iris.target[y!=0]
# print(np.unique(iris_y)) # output array([0, 1, 2])

# np.random.seed(0)
indices = np.random.permutation(len(iris_X))

iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
y_pred = svc.predict(iris_X_test)
print(f"y_pred: {y_pred}")
print(f"y_test: {iris_y_test}")
acc = sum(y_pred == iris_y_test) / len(y_pred)
print(f"acc: {acc}")
