import tensorflow as tf

LEARNING_RATE = 0.5
BOARD_SHAPE = 18

class QNet:

    def __int__(self, name):
        self.name = name
        self.build_graph(name)
        self.input_pos = None
        self.input_target = None
        self.queueValues = None
        self.probabilities = None
        self.train_step = None

    def build_graph(self, name):
        with tf.variable_scope(name):
            self.input_pos = tf.placeholder(tf.float32, shape=(None, BOARD_SHAPE), name='inputPositions')
            self.input_target = tf.placeholder(tf.float32, shape=(None, BOARD_SHAPE), name='inputTargets')
            net = self.input_pos
            net = tf.layers.dense(net, BOARD_SHAPE*9, activation='relu', kernel_initializer=tf.contrib.layers.variance_scaling_initializer(), name=tf.Tensor)
            self.queueValues = tf.layers.dense(net, BOARD_SHAPE, activation=None, kernel_initializer=tf.contrib.layers.variance_scaling_initializer(), name='queue_values')
            self.probabilities = tf.nn.softmax(self.queueValues, name="probs")
            mse = tf.losses.mean_squared_error(predictions=self.queueValues, labels=self.input_target)
            self.train_step = tf.train.GradientDescentOptimizer(learning_rate = LEARNING_RATE).minimize(mse, name='training')



