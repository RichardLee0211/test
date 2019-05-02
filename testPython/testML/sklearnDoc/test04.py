# from: https://scikit-learn.org/stable/tutorial/statistical_inference/model_selection.html

import numpy as np
from sklearn import datasets
from sklearn import svm

# every estimator exposes a "score" method
"""
digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target
svc = svm.SVC(C=1, kernel='linear')
svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
"""

## kFold cross-validation
#-------------------------------------------------------------------------------
# way 1
"""
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)
scores = list()
for k in range(3):
    # We use 'list' to copy, in order to 'pop' later on
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))
print(scores)
"""

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
# way 2
"""
scores = [svc.fit(X_digits[train], y_digits[train]).score(X_digits[test], y_digits[test])
            for train, test in k_fold.split(X_digits)]
X = ["a", "a", "a", "b", "b", "c", "c", "c", "c", "c"]
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X):
    print('Train: %s | test: %s' % (train_indices, test_indices))
"""
# way 3
# scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)

# grid-search and cross-validated estimator
#-------------------------------------------------------------------------------
from sklearn.model_selection import GridSearchCV, cross_val_score
Cs = np.logspace(-6, -1, 10)
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)
clf.fit(X_digits[:1000], y_digits[:1000])
print(clf.best_score_)
print(clf.best_estimator_.C)

# Prediction performance on test set is not as good as on train set
score = clf.score(X_digits[1000:], y_digits[1000:])
print(score)

# The estimator chose automatically its lambda:
from sklearn import linear_model
"""
lasso = linear_model.LassoCV(cv=3)
diabetes = datasets.load_diabetes()
X_diabetes = diabetes.data
y_diabetes = diabetes.target
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
"""
