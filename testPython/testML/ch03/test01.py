from sklearn.datasets import fetch_mldata
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
    mnist = fetch_mldata('MNIST original')
    X, y = mnist["data"], mnist["target"]

    some_digit = X[36000]
    """
    some_digit_image = some_digit.reshape(28, 28)
    plt.imshow(some_digit_image, cmap = matplotlib.cm.binary,
                    # interpolation="nearest")
    plt.axis("off")
    plt.show()
    """

    X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

    shuffle_index = np.random.permutation(60000)
    X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]


    y_train_5 = (y_train == 5) # True for all 5s, False for all other digits
    y_test_5 = (y_test == 5)

    from sklearn.linear_model import SGDClassifier
    sgd_clf = SGDClassifier(random_state=42)
    sgd_clf.fit(X_train, y_train_5)
    # print(sgd_clf.predict([some_digit]))

    from sklearn.model_selection import StratifiedKFold
    from sklearn.base import clone
    skfolds = StratifiedKFold(n_splits=3, random_state=42)

    for train_index, test_index in skfolds.split(X_train, y_train_5):
        clone_clf = clone(sgd_clf)
        X_train_folds = X_train[train_index]
        y_train_folds = (y_train_5[train_index])
        X_test_fold = X_train[test_index]
        y_test_fold = (y_train_5[test_index])

        clone_clf.fit(X_train_folds, y_train_folds)
        y_pred = clone_clf.predict(X_test_fold)
        n_correct = sum(y_pred == y_test_fold)
        print(n_correct / len(y_pred)) # prints 0.9502, 0.96565 and 0.96495

    # from sklearn.model_selection import cross_val_score
    # cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy")


    from sklearn.model_selection import cross_val_predict
    y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)

    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_train_5, y_train_pred)

    from sklearn.metrics import precision_score, recall_score
    precision_score(y_train_5, y_pred) # == 4344 / (4344 + 1307) 0.76871350203503808
    recall_score(y_train_5, y_train_pred) # == 4344 / (4344 + 1077)

    from sklearn.metrics import f1_score
    f1_score(y_train_5, y_pred)

# doing nothing classifier
"""
from sklearn.base import BaseEstimator
class Never5Classifier(BaseEstimator):
    def fit(self, X, y=None):
        pass
    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)

never_5_clf = Never5Classifier()
cross_val_score(never_5_clf, X_train, y_train_5, cv=3, scoring="accuracy")
"""
