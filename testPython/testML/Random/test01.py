# try random.randint against KNN
# not good as expected

import random
from random import randint
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model

# generate a sequence of random numbers in [0, 9]
def generate_sequence(length=25):
    return [randint(0, 9) for _ in range(length)]

# random.seed(0)
N_train = 50000
N_test = 20

if __name__ == "__main__":
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    for _ in range(N_train):
        a = generate_sequence()
        X_train.append(a[:-1])
        y_train.append(a[-1])

    for _ in range(N_test):
        a = generate_sequence()
        X_test.append(a[:-1])
        y_test.append(a[-1])


    # print(f"X_train: {X_train}")
    # print(f"y_train: {y_train}")

    # Create and fit a nearest-neighbor classifier
    # don't do the prediction
    """
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)
    y_correct = (y_pred == y_test)
    print(f"predict: {y_pred}")
    print(f"y_test: {y_test}")
    print(f"y_correct: {y_correct}")
    """

    # linear model
    # don't do the prediction
    """
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    # MSE = np.mean((regr.predict(X_test) - y_test)**2)
    # print(f"MSE: {MSE}")
    y_pred = regr.predict(X_test);
    print(f"y_pred: {y_pred}")
    print(f"y_test: {y_test}")
    score = regr.score(X_test, y_test)
    print(f"score: {score}")
    """
