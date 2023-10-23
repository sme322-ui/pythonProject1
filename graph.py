from sklearn.datasets import make_regression
from matplotlib import pyplot
from sklearn.datasets import make_blobs
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import tensorflow as tf
model = LinearRegression()
import keras.backend as K

import numpy as np
heights = [[1.6],[1.65],[1.7],[1.73],[1.8]]
weights = [[60],[65],[72.3],[75],[80]]
model.fit(X=heights,y=weights)
pyplot.plot(heights,weights,'k.')
pyplot.title('Weight plotted against heights')
pyplot.xlabel('Observe value')
pyplot.ylabel('expect times')
pyplot.axis([1.5,1.85,50,90])

pyplot.grid(True)
pyplot.plot(heights,model.predict(heights),color='r')
print('Residual sum of squares: %.2f' % np.sum((weights - model.predict(heights))**2))

pyplot.show()
print('回歸截距: w0={}'.format(model.intercept_[0],2))
print('回歸系数: w1={}'.format(model.coef_[0][0],2))
message = tf.constant("Hello World!")
tf.compat.v1.disable_eager_execution()
hello=tf.constant('Hello,TensorFlow')
config=tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9
sess=tf.compat.v1.Session(config=config)
print(sess.run(hello))
print(K.epsilon())