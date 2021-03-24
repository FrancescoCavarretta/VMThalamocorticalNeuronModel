from header import *

import pyneuron
import numpy as np

def sim(cell, ic_holding, ic_stimulus, ic_stim_delay=5000.0, ic_stim_dur=2000.0, tstop=None, vinit=-78):
  
  tstop = ic_stim_delay*2+ic_stim_dur if tstop is None else tstop
  
  try:
    _soma_ref = cell.soma[0]
  except TypeError:
    _soma_ref = cell.soma


  recording = set_recording(_soma_ref(0.5)._ref_v)

  ic_hold       = h.IClamp(0.5, sec=_soma_ref)
  ic_hold.delay = 0
  ic_hold.dur   = tstop
  ic_hold.amp   = ic_holding
  
  ic_stim       = h.IClamp(0.5, sec=_soma_ref)
  ic_stim.delay = ic_stim_delay
  ic_stim.dur   = ic_stim_dur
  ic_stim.amp   = ic_stimulus
  
  run(tstop, vinit=vinit)


  return pyneuron.vector_to_ndarray(recording[0]), \
         pyneuron.vector_to_ndarray(recording[1])


def sim_batch(cell, ic_holding, ic_stim, ic_stim_delay=2000.0, ic_stim_dur=2000.0, tstop=None, vinit=-78):

  def check_arg(ic):
    if type(ic) == int:
      ic += 0.
    if type(ic) == float or type(ic) == np.float64:
      ic = [ ic ]
    #print (ic,type(ic))
    assert type(ic) == list or type(ic) == np.ndarray
    return ic

  
  ic_holding = check_arg(ic_holding)
  ic_stim    = check_arg(ic_stim)

  recording = []
  for i in range(len(ic_holding)):
    for j in range(len(ic_stim)):
      recording.append(
        sim(cell,
          ic_holding[i],
          ic_stim[j],
          ic_stim_delay=ic_stim_delay,
          ic_stim_dur=ic_stim_dur,
          tstop=tstop,
          vinit=vinit)
      )

  return recording



def get_holding_current(cell, vm, ic_min=0.01, ic_max=0.35, ic_inc=0.01):
  ic = np.arange(ic_min, ic_max+ic_inc, ic_inc)
  
  cell.soma[0].push(); apc = h.APCount(0.5); h.pop_section()
  
  i_min = 0
  i_max = len(ic)
  
  while i_min <= i_max:
    apc.n = 0.
    i = int((i_min+i_max)/2)
    
    sim(cell, ic[i], 0, tstop=5000.0)

    if apc.n > 0:
      i_max = i-1
    elif cell.soma[0].v < vm:
      i_min = i+1
    elif cell.soma[0].v > vm:
      i_max = i-1
    else:
      break
      

  return ic[i+1]
    

  
