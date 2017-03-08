import pysynth
import numpy
import pysynth_b

test = (('g#4', 2), ('r', 4))

pysynth_b.make_wav(test, fn = "g#42.wav")
