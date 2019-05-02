# from: https://scikit-learn.org/stable/tutorial/statistical_inference/unsupervised_learning.html

# k-means
#-------------------------------------------------------------------------------
from sklearn import datasets
from sklearn import cluster
"""
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target

k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

print(k_means.labels_[::10]) # include labels_[10]
print(y_iris[::10])
"""
## Connectivity-constrained clustering
# TODO: don't really understand this
#-------------------------------------------------------------------------------
"""
import matplotlib.pyplot as plt

from skimage.data import coins
from skimage.transform import rescale

from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import AgglomerativeClustering
# #############################################################################
# Generate data
orig_coins = coins()

# Resize it to 20% of the original size to speed up the processing
# Applying a Gaussian filter for smoothing prior to down-scaling
# reduces aliasing artifacts.
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect")

X = np.reshape(rescaled_coins, (-1, 1))

# #############################################################################
# Define the structure A of the data. Pixels connected to their neighbors.
connectivity = grid_to_graph(*rescaled_coins.shape)
"""

## Feature agglomeration
#-------------------------------------------------------------------------------
"""
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
connectivity = grid_to_graph(*images[0].shape)

agglo = cluster.FeatureAgglomeration(connectivity=connectivity,
                                             n_clusters=32)
agglo.fit(X)

X_reduced = agglo.transform(X)

X_approx = agglo.inverse_transform(X_reduced)
images_approx = np.reshape(X_approx, images.shape)
"""

# TODO: in this page
#   - Principal Component Analysis: PCA
#   - Independent Component Analysis: ICA
