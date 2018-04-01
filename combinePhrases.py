import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np

# This file will generate combinations of phrases based
# on their classification as a specific type of phrase
# Sample:
# [ Phrase T 1, Phrase T 2, Phrase T 3, ... ]
# [ 0,        , 0.5,      , 0.5] => each of these should sum to one
# 
# and in this case we look at the preceding phrase and following phrase
# to try to determine what kind of phrase we want next

# in this case, the len of each row is the types of phrases we've identified

def createSample(num_phrase_types, testPhrases, lr=tf.constant(0.005), training_steps=1000, batch_size=50):
  time_steps = 32
  num_hidden = np.shape(testPhrases)[0]
  num_input = np.shape(testPhrases)[0]
  x = tf.placeholder(tf.float32, [None,timesteps, num_input])
  y = tf.placeholder(tf.float32, [None, num_phrase_types])

  def BiRNN(inp, weights, biases):
    inp = tf.unstack(inp, timestep, 1)
    assert tf.shape(inp)[:2] == (time_steps, num_input)
    # do these need to be the same
    lstm_forward = rnn.BasicLSTMCell(num_hidden)
    lstm_backward = rnn.BasicLSTMCell(num_hidden)

    outputs, output_states = tf.nn.bidirectional_dynamic_rnn(
       cell_fw=lstm_forward,
       cell_bw=lstem_backward,
       inputs=inp,
       dtype=tf.float32
    )
    output_fw, output_bw = outputs
    return tf.matmul(output_bw, weights['out']) +  biases['out']
    # output is in the form [batch_size, timesteps, lstm_forward.outputSize(numhidden)]
    # output is num_input x timesteps 

  # https://en.wikipedia.org/wiki/Logit
  logit = BiRNN(x, w, b)
  prediction = tf.nn.sigmoid(logits)

  loss_op = tf.nn.sigmoid_cross_entropy_with_logits(logits=logit, labels=y)

  optimizer = tf.train.AdamOptimizer(learning_rate=lr)
  train_op = optimizer.minimize(loss_op)

  correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

  init = tf.global_variables_initializer()

  with tf.Session() as sess:
    sess.run(init)
    for step in range(1, training_steps+1):
      for phrase_collection, phrase_labels in testPhrases:
        phraseCollection = np.array(phrase_collection)
        phraseCollection = np.reshape((batch_size, time_steps, num_input))
        sess.run(train_op, feed_dict={x: phrase_collection, y:phrase_labels}

    x_sample = SOME_GENERATED PHRASES

    FINAL_RESULT = prediction.eval(feed_dict={x: x_sample}, session=sess)
    print(FINAL_RESULT)
