import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn

# hyperparameters
learning_rate = 0.001
batch_size = 10
num_steps = 10

# neural net parameters
# num of visible nodes must match input size or input size must be truncated
# size of hidden layer is expected number of outputs (which in this case is set of all possible notes
# there must be a weight vector for the cost of going between the edges
# there must be a bias vector for all layers
num_hidden = 128
num_input = 28
time_steps = 28

notes = tf.placeholder(tf.float32, [batch_size, num_steps])

# so there's a bias layer for the visible level, hidden level
# as well as a weight layer for each level to the next
# timesteps is equivalent to how long the neural network can remember things

# long short term memory
x = tf.placeholder(tf.float32, INPUT_SIZE)
y = tf.placeholder(tf.float32, NONE) # todo

hidden_state = tf.zeros([batch_size, lstm_size])
initial_state = tf.zeros([batch_size, lstm_size])
state = hidden_state, current_state
probabilities = []
loss = 0.0

# this session will evaluate all tensors

np_state = initial_state.eval()

for note_batch in notes:
  output, state = lstm(note_batch, state)


def RNN(x, weights, bias):
  x = tf.unstack(x, timesteps, 1)
  lstm_cell = rnn.BasicLSTMCell(num_hidden, forget_bias=1.0)
  outputs, states = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)

  return outputs


# matrix x from dataset, weights, bias hidden, bias_visible, hidden function,  learning rate
def constrastive_divergence(x, w, bh, bv, h, lr=0.0001):
  # get sample of x
  res_w = tf.add(w, tf.mul(lr, tf.sub(tf.mul(np.transpose(x), h(x)), tf.mul(np.transpose(sX, h(sX))))))
  res_bh = tf.add(bh, tf.mul(lr, tf.sub(h(x),h(sX))))
  res_bv = tf.add(bv, tf.mul(lr, tf.sub(x,sX)))

