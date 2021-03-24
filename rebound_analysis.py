import fi_curve_analysis as FI
from pynwb import NWBHDF5IO
import numpy as np
import efel
import analysis

def get_deflection(nwbfile,
                    fmtkey,
                    ic_stim,
                    stim_start=5000,
                    stim_end=7000):
  
  ii = []
  dd = []

  for _ic_stim in ic_stim:
    trace = analysis.read_trace(nwbfile, fmtkey % _ic_stim, stim_start=stim_start, stim_end=stim_end)
    ii.append(
      _ic_stim
    )
##    try:
##    v = np.interp(np.arange(stim_start, stim_end, 0.01), trace['T'], trace['V'])
    
    dd.append(
      efel.getFeatureValues([trace],['voltage_deflection'])[0]['voltage_deflection'][0]
    )
##    print (dd[-1])
##    except:
##      import matplotlib.pyplot as plt
##      plt.plot(trace['T'], trace['V'])
##      plt.show()

  print ("done")

  return ii, dd
  
def get_rebound_spk(nwbfile,
                    fmtkey,
                    ic_stim,
                    stim_start=5000,
                    stim_end=7000,
                    tshift_init=0,
                    tshift_end=2000,
                    duration=[200,500,2000]):


  spk = {}

  for dur in duration:
    ii, ff = FI.get_fi_curve(nwbfile,
                    fmtkey+'_'+str(dur),
                    ic_stim,
                    stim_start=(stim_start+dur),
                    stim_end=(stim_start+dur+tshift_end),
                    tshift=0)
    dd = get_deflection(nwbfile,
                    fmtkey+'_'+str(dur),
                    ic_stim,
                    stim_start=stim_start,
                    stim_end=(stim_start+dur))[1]

    spk[dur] = (np.array(dd), np.array(ff))

  print ("done")
  return spk
    


def get_avg_spk(spk, defs=[(-20,0),(-60,-40),(-80,-60)]):

  hist = {}
  
  for dur, data in spk.items():
    hist[dur] = {}
    for _def in defs:
      dd, ff = data
      print (dd,ff)
      freqs = ff[np.logical_and(dd >= _def[0], dd < _def[1])]
      hist[dur][_def] = (np.mean(freqs), np.std(freqs))

  return hist
      
    


if __name__ == '__main__':
  io = NWBHDF5IO('rebound.nwb', 'r')
  nwbfile = io.read()


  import matplotlib.pyplot as plt
  spk = get_rebound_spk(nwbfile, "control_%g", np.arange(0.025, 0.5, 0.025))
  avgspk = get_avg_spk(spk)

  for dur, nspk in avgspk.items():
    for _def, _nspk in nspk.items():
      __def=(abs(_def[1]),abs(_def[0]))
      print ('%g-%g %g %g'%(__def+_nspk))
