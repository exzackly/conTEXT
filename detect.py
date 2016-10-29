from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time

import numpy as np
import tensorflow as tf

import rnn

flags = tf.flags

flags.DEFINE_bool("test", False, "")
flags.DEFINE_string(
    "model", "small",
    "A type of model. Possible options are: small, medium, large.")
flags.DEFINE_string("data_path", "data/",
                    "Where the training/test data is stored.")
flags.DEFINE_string("save_path", "save/",
                    "Model output directory.")
flags.DEFINE_bool("use_fp16", False,
                  "Train using 16-bit floats instead of 32bit floats")

FLAGS = flags.FLAGS

rnn.init(flags.FLAGS)

if FLAGS.test:
  print(rnn.test_words(" Oh right; thanks Oh right; thanks Oh right; thanks Oh right; thanks Oh right; thanks Oh right; thanks Oh right; thanks Oh right; thanks Oh right; thanks Oh right; thanks Oh right; thanks"))
  print(rnn.test_words(" hi! how are u?? hi! how are u?? hi! how are u?? hi! how are u?? hi! how are u?? hi! how are u?? hi! how are u?? hi! how are u?? hi! how are u?? hi! how are u?? hi! how are u??"))
else:
  rnn.main()
