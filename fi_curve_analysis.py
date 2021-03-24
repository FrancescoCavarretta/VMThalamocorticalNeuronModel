from pynwb import NWBHDF5IO
import numpy as np
import efel
from scipy.stats import linregress
import analysis


def get_fi_curve(nwbfile, fmtkey, ic_stim, stim_start=2000, stim_end=4000, tshift=50):
  ii = []
  ff = []

  for _ic_stim in ic_stim:
    trace = analysis.read_trace(nwbfile, fmtkey % _ic_stim, stim_start=stim_start, stim_end=stim_end)
    trace['stim_start'][0] += tshift

    ii.append(
      _ic_stim
    )
    ff.append(
      efel.getFeatureValues([trace], ['Spikecount'])[0]['Spikecount'][0]/(stim_end-stim_start-tshift)*1000.0
    )


  return np.array(ii).T, np.array(ff).T





def get_rheobase(ii, ff, freq=3.0):
  ii, ff = _get_rheobase_1(ii, ff)
  slope, intercept = linregress(ii, y=ff)[:2]
  return np.ceil((freq-intercept)/slope*100)/100.


def _get_rheobase_1(ii, ff):
  imin = np.argwhere(ff > 0)[0][0]
  ii = ii[imin:]
  ff = ff[imin:]
  return ii, ff


def spike_threshold(nwbfile, fmt, ic_stim, stim_start=2000, stim_end=4000, tshift=50, newDerivativeThreshold=10.0):
  ii, ff = get_fi_curve(nwbfile, fmt, np.arange(0.01, 0.37, 0.01))
  _rheobase_ii = _get_rheobase_1(ii, ff)[0][0]
  efel.api.setDerivativeThreshold(newDerivativeThreshold)
  return efel.getFeatureValues([read_trace(nwbfile, (fmt + "_%g") % _rheobase_ii)], ['AP1_begin_voltage'])[0]['AP1_begin_voltage'][0]

  


if __name__ == '__main__':
  io = NWBHDF5IO('fi_curve.nwb', 'r')
  nwbfile = io.read()


  import matplotlib.pyplot as plt
  ii, ff = get_fi_curve(nwbfile, "km0_%g", np.arange(0.01, 0.37, 0.01))
  plt.plot(ii, ff, 'r')
##  ii, ff = get_fi_curve(nwbfile, "km0.5_%g", np.arange(0.01, 0.37, 0.01))
##  plt.plot(ii, ff, 'g')
  ii, ff = get_fi_curve(nwbfile, "control_%g", np.arange(0.01, 0.37, 0.01))
  plt.plot(ii, ff)
  plt.show()


##  ii, ff = get_fi_curve(nwbfile, "ih1.7_%g", np.arange(0.01, 0.37, 0.01))
##  plt.plot(ii, ff, 'r')
##  ii, ff = get_fi_curve(nwbfile, "ih1.35_%g", np.arange(0.01, 0.37, 0.01))
##  plt.plot(ii, ff, 'g')
##  ii, ff = get_fi_curve(nwbfile, "control_%g", np.arange(0.01, 0.37, 0.01))
##  plt.plot(ii, ff)
##  plt.show()  

