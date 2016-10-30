from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time

import numpy as np
import tensorflow as tf

import rnn
import prepare
import xml_parser as xp

class Args:
  pass

class Flags:
  pass

FLAGS = Flags()

# Set parameters for the neural network
FLAGS.model = 'test'
FLAGS.data_path = 'data/'
FLAGS.save_path = 'save/'
FLAGS.use_fp16 = False
FLAGS.test = True

rnn.init(FLAGS)

# Get per word perplexity for the sample text
def test(text):
  rnn.FLAGS.test = True
  return rnn.test_words(text)

def train(name):
  rnn.FLAGS.test = False
  # Extract messages from Facebook Messenger data
  xp.extract_messages(name + '.htm', name + '.txt', name)
  args = Args()
  args.infile = name + '.txt'
  args.out_dir = FLAGS.data_path
  args.vocab_size = 20000
  args.frequency = False
  # Prepare the extracted messages for neural net training
  prepare.process_file(args)
  rnn.main()
