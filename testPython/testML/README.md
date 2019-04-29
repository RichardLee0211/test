Hands-on Machine Learning with Scikit-Learn and TensorFlow
================================================================================

reference code: https://github.com/ageron/handson-ml

on page.5:
large data is not a problem, Orgainzation would have millions of users, they manage it.

ch01 The ML landscape
--------------------------------------------------------------------------------

Supervised Learning:
- kNN
- Linear Regression
- Logistic Regression
- Support Vector Machines(SVMs)
- Decision Trees and Random Forests
- Neural networks

Unsupervised Learning:
- Clustering
    + k-Means
    + Hierarchical Cluster Analysis(HCA)
    + Expectation Maximization
- Visualization and dimensionality reduction
    + Principal Component Analysis(PCA)
    + Kernel PCA
    + Locally-Linear Embedding(LLE)
    + t-distributed Stochastic Neighbor Embedding(t-SNE)
- Association rule learning
    + Apriori
    + Eclat
- Semisupervised Learning
- Reinforcement Learning

ENGLISH: Finally, if your system needs to be able to learn autonomously and it has limited resources (e.g., a smartphone application or a rover on Mars), then carrying around large amounts of training data and taking up a lot of resources to train for hours every day is a showstopper.

.ipynb file is like put code, README, and pic all togother
separation have its own advantages
integral have its own advantages
as a 60% software engineer, I would choice formar

TODO_2: page.23, maybe reading these paper?
TODO_2: page.30, No Free Lunch(NFL) theorem

ch02 End-to-End Machine Learning Project
--------------------------------------------------------------------------------
supervised, unsupervised, or Reinforcement Learning
classification task, a regression task, or something else
batch learning or online learning techniques

about hand-writing Matrix or vector notation: https://math.stackexchange.com/questions/1292540/matrix-notation-in-handwriting
could be under-line or repeated parts

RMSE: Root Mean Square Error
MAE: Mean Absolute Error

longitude,latitude,
housing_median_age,total_rooms,total_bedrooms,
population,households,median_income,median_house_value,ocean_proximity

TODO: df.iloc[ndarray]

page.63, This is called one-hot encoding, because only one attribute will be equal to 1 (hot), while the others will be 0 (cold).

TODO: be to continue
