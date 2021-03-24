from neuron import h
h.load_file("AA0136.hoc")

h.load_file("stdrun.hoc")

cell = h.AA0136()

import edyta_sim
import numpy as np
import pynwb_io
import pyneuron

h.cvode_active(1)

h.celsius = 27.0

def run(tstop, vinit=-78):
  h.tstop = tstop
  h.v_init = vinit
  h.run()


def set_recording(_ref_v):
  t_vec = h.Vector()
  v_vec = h.Vector()
  h.cvode.record(_ref_v, v_vec, t_vec)
  return t_vec, v_vec
