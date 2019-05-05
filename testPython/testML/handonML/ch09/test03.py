# manual gradient Descent
# TODO: check_point_save: https://stackoverflow.com/questions/45179556/key-variable-name-not-found-in-checkpoint-tensorflow

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import tensorflow as tf
import numpy as np
from sklearn.datasets import fetch_california_housing

""" data """
housing = fetch_california_housing()
m, n = housing.data.shape
housing_data = housing.data
data_max = housing_data.max(axis=0)
data_min = housing_data.min(axis=0)
housing_data = (housing_data-data_min) / (data_max - data_min)
housing_data_plus_bias = np.c_[np.ones((m, 1)), housing_data]

""" parameter """
n_epochs = 1000
chs = 1000
learning_rate = 0.01

""" graph """
# X = tf.constant(scaled_housing_data_plus_bias, dtype=tf.float32, name="X")
X = tf.constant(housing_data_plus_bias, dtype=tf.float32, name="X")
y = tf.constant(housing.target.reshape(-1, 1), dtype=tf.float32, name="y")
theta = tf.Variable(tf.random_uniform([n + 1, 1], -1.0, 1.0), name="theta")
y_pred = tf.matmul(X, theta, name="predictions")
error = y_pred - y
mse = tf.reduce_mean(tf.square(error), name="mse")
# gradients = 2/m * tf.matmul(tf.transpose(X), error)
# training_op = tf.assign(theta, theta - learning_rate * gradients)
### replace this two lines with pre-build optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
training_op = optimizer.minimize(mse)
init = tf.global_variables_initializer()
saver = tf.train.Saver()

""" run """
with tf.Session() as sess:
    sess.run(init)
    # saver.restore(sess, "/tmp/my_model.ckpt")
    ### normal train
    """
    for epoch in range(n_epochs):
        if epoch%100==0:
            print("Epoch", epoch, "MSE =", mse.eval())
        sess.run(training_op)
    best_theta = theta.eval()
    """

    ### test train
    """
    """
    for epoch in range(100):
        sess.run(training_op)
        if epoch%20  == 0 :
            print("MSE =", mse.eval())
            # best_theta = theta.eval()
    save_path = saver.save(sess, "/tmp/my_model.ckpt")
