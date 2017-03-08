import pysynth
import numpy
import pysynth_b

test = (('g#3', 8), ('r', 4))

pysynth_b.make_wav(test, fn = "g#3.wav")
