import tensorflow as tf
x = tf.Variable(3, name="x")
y = tf.Variable(4, name="y")
f=x*x*y+y+2

sess = tf.Session()
sess.run(x.initializer)
sess.run(y.initializer)
result = sess.run(f)
print(result)
sess.close()

# clearer code
with tf.Session() as sess:
    x.initializer.run()
    y.initializer.run()
    result = f.eval()

# or another way, tf.global_variables_initializer()
init = tf.global_variables_initializer() # prepare an init node
with tf.Session() as sess:
    init.run() # actually initialize all the variables
    result = f.eval()

# interavtiveSession
sess = tf.InteractiveSession()
init.run()
result = f.eval()
print(result)
sess.close()

# manage graph
#-------------------------------------------------------------------------------
x1 = tf.Variable(1)
x1.graph is tf.get_default_graph()  # True

# add note to another graph
graph = tf.Graph()
with graph.as_default():
    x2 = tf.Variable(2)

x2.graph is graph # True
x2.graph is tf.get_default_graph() # False
