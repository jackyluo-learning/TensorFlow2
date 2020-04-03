import tensorflow as tf
import tensorflow_addons as tfa


class policy_network(tf.keras.Model):
    def __init__(self, max_layers):
        super(policy_network, self).__init__()
        self.max_layers = max_layers
        nas_cell = tfa.rnn.NASCell(4 * max_layers)
        self.model = tf.keras.layers.RNN(cell=nas_cell, input_shape=[None, 4*max_layers])


    def call(self, inputs, training=None, mask=None):
        inputs = tf.expand_dims(inputs, -1)
        outputs = self.model(inputs)
        self.x = outputs
        # print("outputs: ", outputs, outputs[:, -1:, :],
        #       tf.slice(outputs, [0, 4 * self.max_layers - 1, 0], [1, 1, 4 * self.max_layers]))
        # return tf.slice(outputs, [0, 4*max_layers-1, 0], [1, 1, 4*max_layers]) # Returned last output of rnn
        return outputs

