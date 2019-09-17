import tensorflow as tf

greeting = tf.constant('Hello Google Tensorflow!')
sess = tf.Session()
result = sess.run(greeting)
print(result)
sess.close()