from pynwb import NWBHDF5IO
import numpy as np
import efel
from scipy.stats import linregress
import analysis


def get_sag_curve(nwbfile, fmtkey, ic_stim, stim_start=5000, stim_end=7000):
  ii = []
  ss = []

  for _ic_stim in ic_stim:
    trace = analysis.read_trace(nwbfile, fmtkey % abs(_ic_stim), stim_start=stim_start, stim_end=stim_end)

    ii.append(
      _ic_stim
    )
    ss.append(
      100*(1-efel.getFeatureValues([trace], ['sag_ratio2'])[0]['sag_ratio2'][0])
    )


  return np.array(ii).T, np.array(ss).T





  


if __name__ == '__main__':
  io = NWBHDF5IO('sag.nwb', 'r')
  nwbfile = io.read()


  import matplotlib.pyplot as plt
  ii, ss = get_sag(nwbfile, "km0_%g", np.arange(0.05, 0.2, 0.05))
  plt.plot(ii, ss)
  ii, ss = get_sag(nwbfile, "control_%g", np.arange(0.05, 0.2, 0.05))
  plt.plot(ii, ss, 'r')
  ii, ss = get_sag(nwbfile, "ih1.35_%g", np.arange(0.05, 0.2, 0.05))
  plt.plot(ii, ss, 'g')
  plt.show()


