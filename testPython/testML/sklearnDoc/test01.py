# from: https://scikit-learn.org/stable/tutorial/basic/tutorial.html

## model persistence
from sklearn import svm
from sklearn import datasets
clf = svm.SVC(gamma='scale')
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)
"""
output in ipython :
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
        decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
        max_iter=-1, probability=False, random_state=None, shrinking=True,
        tol=0.001, verbose=False)
"""

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print(clf2.predict(X[0:1]))
print(y[0])

# or use joblib
"""
from joblib import dump, load
dump(clf, 'filename.joblib')
load(clf, "filename.joblib")
"""

# Calling fit() more than once will overwrite what was learned by any previous fit()
import numpy as np
from sklearn.svm import SVC

rng = np.random.RandomState(0)
X = rng.rand(100, 10)
y = rng.binomial(1, 0.5, 100)
X_test = rng.rand(5, 10)

clf = SVC()
clf.set_params(kernel='linear').fit(X, y)
clf.predict(X_test)

clf.set_params(kernel='rbf', gamma='scale').fit(X, y)
clf.predict(X_test)
