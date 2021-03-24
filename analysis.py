
import numpy as np

def read_trace(nwbfile, key, stim_start=2000, stim_end=4000):
  ephys_ts = nwbfile.acquisition[key]
  return {
    'T':np.array(ephys_ts.timestamps),
    'V':np.array(ephys_ts.data),
    'stim_start':[stim_start],
    'stim_end':[stim_end]
  }
