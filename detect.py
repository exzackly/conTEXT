from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time

import numpy as np
import tensorflow as tf

import rnn
import prepare
import xml_parser as xp

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

class Args:
  pass

if FLAGS.test:
  #rnn.get_test_session()
  #print(rnn.test_words(" 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 "))
  #print(rnn.test_words("That was <unk> lovely; I look forward to it being <unk> at Bardavon this spring. I am happy to report that I have extended my flute range to F# ( yes , the fourth one )"))
  #print(rnn.test_words("That was <unk> lovely; I lok frward to it bing <unk> at Brdavon this sping. I am appy to reort tha I have xtended my flute range to F# ( yes , the fourth one )"))
  print(rnn.test_words(" Hello; my name is Brendon. If you do not believe this is me -- well there is nothing I can do about that. I wish you the best."))
  print(rnn.test_words("hiya why would u think it's me?? do i really type like this at all; i dont know why this isn't workin at all. it makes me sooo sad "))
else:
  xp.extract_messages('messages.htm', 'messages.txt', 'Brendon Boldt')
  args = Args()
  args.infile = 'messages.txt'
  #args.outfile = FLAGS.data_path + 'tokens.txt'
  args.out_dir = FLAGS.data_path
  args.vocab_size = 20000
  args.frequency = False
  prepare.process_file(args)
  rnn.main()
