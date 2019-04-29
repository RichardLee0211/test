## this is more like a back-up code for review and learning
import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hashlib

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

def split_train_test(data, test_ratio):
    np.random.seed(42)
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

# TODO: fancy python programming
def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]

from sklearn.base import BaseEstimator, TransformerMixin
rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self # nothing else to do

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

# usage
# attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
# housing_extra_attribs = attr_adder.transform(housing.values)

from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names=attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values


if __name__ == "__main__":
    # fetch_housing_data()
    housing = load_housing_data()
    # housing.head()
    # housing.info()
    # housing["ocean_proximity"].value_counts()
    # housing.describe()
    # housing.hist(bins=50, figsize=(20,15))
    # plt.show()

    # one way
    # housing_with_id = housing.reset_index() # adds an `index` column
    # train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")
    # or another
    # housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
    # train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")
    # or another
    # from sklearn.model_selection import train_test_split
    # train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

    # or another
    """
    housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
    housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
    from sklearn.model_selection import StratifiedShuffleSplit
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    for set in (strat_train_set, strat_test_set):
        set.drop(["income_cat"], axis=1, inplace=True)
    """

    # it is true that this plot module is slow and don't have shortcut to explore virsual data
    # housing = strat_train_set.copy()
    # housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
    """
    housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
                s=housing["population"]/100, label="population", # s, radius, c, color
                c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
                )
    """
    # plt.legend()
    # plt.show()

    # corr_matrix = housing.corr()
    # corr_matrix["median_house_value"].sort_values(ascending=False)

    """
    from pandas.tools.plotting import scatter_matrix
    attributes = ["median_house_value", "median_income", "total_rooms",
                "housing_median_age"]
    scatter_matrix(housing[attributes], figsize=(12, 8))
    """
    # housing.pop # TODO: remove sample where median_income=4500
    # housing.plot(kind="scatter", x="median_income", y="median_house_value",
                             # c="red", alpha=0.1)
    # plt.show()

    ## add some new combine feature
    # housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
    # housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
    # housing["population_per_household"]=housing["population"]/housing["households"]
    # corr_matrix = housing.corr()
    # corr_matrix["median_house_value"].sort_values(ascending=False)

    # housing = strat_train_set.drop("median_house_value", axis=1)
    # housing_labels = strat_train_set["median_house_value"].copy()

    ## deal with missing value
    # option 1
    # housing.dropna(subset=["total_bedrooms"])
    # option 2
    # housing.drop("total_bedrooms", axis=1)
    # option 3
    # median = housing["total_bedrooms"].median()
    # housing["total_bedrooms"].fillna(median)


    from sklearn.preprocessing import Imputer
    """
    imputer = Imputer(strategy="median")
    housing_num = housing.drop("ocean_proximity", axis=1)
    imputer.fit(housing_num)
    # imputer.statistics_
    X = imputer.transform(housing_num)
    housing_tr = pd.DataFrame(X, columns=housing_num.columns)
    """

    ## handle category data
    from sklearn.preprocessing import LabelEncoder
    """
    encoder = LabelEncoder()
    housing_cat = housing["ocean_proximity"]
    housing_cat_encoded = encoder.fit_transform(housing_cat)

    from sklearn.preprocessing import OneHotEncoder
    encoder = OneHotEncoder()
    housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
    """

    # or in one move
    from sklearn.preprocessing import LabelBinarizer
    # encoder = LabelBinarizer()
    # housing_cat_1hot = encoder.fit_transform(housing_cat)

    ## using pipeline
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    """
    num_pipeline = Pipeline([
            ('imputer', Imputer(strategy="median")),
            ('attribs_adder', CombinedAttributesAdder()),
            ('std_scaler', StandardScaler()),
                            ])
    housing_num = housing.drop("ocean_proximity", axis=1)
    housing_num_tr = num_pipeline.fit_transform(housing_num)
    """

    ## using Feature Union
    from sklearn.pipeline import FeatureUnion
    """
    housing_num = housing.drop("ocean_proximity", axis=1)
    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"]
    num_pipeline = Pipeline([
            ('selector', DataFrameSelector(num_attribs)),
            ('imputer', Imputer(strategy="median")),
            ('attribs_adder', CombinedAttributesAdder()),
            ('std_scaler', StandardScaler()),
            ])
    cat_pipeline = Pipeline([
            ('selector', DataFrameSelector(cat_attribs)),
            ('label_binarizer', LabelBinarizer()),
            ])
    full_pipeline = FeatureUnion(transformer_list=[
            ("num_pipeline", num_pipeline),
            ("cat_pipeline", cat_pipeline),
            ])
    housing_prepared = full_pipeline.fit_transform(housing) # a problem in pipeline.py,scikit-learn version problem, 0.18.0 0.20.0
    """

    ## train
    # from sklearn.linear_model import LinearRegression lin_reg = LinearRegression()
    # lin_reg.fit(housing_prepared, housing_labels)

    some_data = housing.iloc[:5]
    some_labels = housing_labels.iloc[:5]
    some_data_prepared = full_pipeline.transform(some_data)
    print("Predictions:\t", lin_reg.predict(some_data_prepared))
    # Predictions: [ 303104. 44800. 308928. 294208. 368704.]
    print("Labels:\t\t", list(some_labels))
    # Labels: [359400.0, 69700.0, 302100.0, 301300.0, 351900.0]

    from sklearn.metrics import mean_squared_error
    housing_predictions = lin_reg.predict(housing_prepared)
    lin_mse = mean_squared_error(housing_labels, housing_predictions) >>> lin_rmse = np.sqrt(lin_mse)
    # lin_rmse
    # 68628.413493824875

    from sklearn.tree import DecisionTreeRegressor
    tree_reg = DecisionTreeRegressor()
    tree_reg.fit(housing_prepared, housing_labels)

    housing_predictions = tree_reg.predict(housing_prepared)
    tree_mse = mean_squared_error(housing_labels, housing_predictions) >>> tree_rmse = np.sqrt(tree_mse)
    # tree_rmse
    # 0.0

    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(tree_reg, housing_prepared, housing_labels,
                            scoring="neg_mean_squared_error", cv=10)
    rmse_scores = np.sqrt(-scores)

    def display_scores(scores):
        print("Scores:", scores)
        print("Mean:", scores.mean())
        print("Standard deviation:", scores.std())

    display_scores(tree_rmse_scores)
    """
    Scores: [ 74678.4916885 64766.2398337 69632.86942005 69166.67693232
            71486.76507766  73321.65695983  71860.04741226  71086.32691692
            76934.2726093   69060.93319262]
    Mean: 71199.4280043
    Standard deviation: 3202.70522793
    """

    ## TODO: save and load models
    """
    from sklearn.externals import joblib
    joblib.dump(my_model, "my_model.pkl")
    # and later...
    my_model_loaded = joblib.load("my_model.pkl")
    """

    from sklearn.model_selection import GridSearchCV
    param_grid = [
                {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
                {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
                ]
    forest_reg = RandomForestRegressor()
    grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                            scoring='neg_mean_squared_error')
    grid_search.fit(housing_prepared, housing_labels)
    # >>> grid_search.best_params_
    # {'max_features': 6, 'n_estimators': 30}
    # >>> cvres = grid_search.cv_results_
    # ... for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    # ...   print(np.sqrt(-mean_score), params)

    ## test on test set
    final_model = grid_search.best_estimator_
    X_test = strat_test_set.drop("median_house_value", axis=1)
    y_test = strat_test_set["median_house_value"].copy()
    X_test_prepared = full_pipeline.transform(X_test)
    final_predictions = final_model.predict(X_test_prepared)
    final_mse = mean_squared_error(y_test, final_predictions)
    final_rmse = np.sqrt(final_mse) # => evaluates to 48,209.6
