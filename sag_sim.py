from pynwb import NWBHDF5IO
import edyta_sim
from header import cell, pynwb_io
import numpy as np





def get_sag_curves(out, key, ic_min, ic_max, ic_step, ic_holding):
  ic_stim = np.arange(ic_min, ic_max+ic_step, ic_step)
  
  recording = edyta_sim.sim_batch(cell,
                      ic_holding,
                      ic_stim,
                      ic_stim_delay=5000.0,
                      ic_stim_dur=2000,
                      vinit=-77.3)


  for i, data in enumerate(recording):
    out.write((key+"_%g")%abs(ic_stim[i]),
              data[0],
              data[1],
              ("hold=%gnA,stim=%gnA"%(ic_holding, ic_stim[i])))
  print ("done")


  
if __name__ == '__main__':
  import os
  import pickle
  
  gmax_iM = cell.get_km()
  gmax_iH = cell.get_h()
  
  holding_current = {}

##  if os.path.exists('ic_75mv.pkl'):
##    with open('ic_75mv.pkl', 'rb') as fi:
##      holding_current = pickle.load(fi)
##  else:
##
  holding_current['control'] = 0
##    
  for perc in [0, 0.5]:
##    cell.set_km(gmax_iM*perc, 50)
    holding_current['km%g'%perc] = 0
##    cell.set_km(gmax_iM, 50)
##
  for perc in [2, 3.0 ]:
##    cell.set_h(gmax_iH*perc)
    holding_current['ih%g'%perc] = 0
##    cell.set_h(gmax_iH)
##
##    cell.set_km(gmax_iM*perc, 50)
  for perc in [2, 3.0 ]:
##      cell.set_h(gmax_iH*perc)
    holding_current['km0ih%g'%perc] = 0
##      cell.set_h(gmax_iH)
##    cell.set_km(gmax_iM, 50)
##    
##    with open('ic_75mv.pkl', 'wb') as fo:
##      pickle.dump(holding_current, fo)




  out = pynwb_io.My_NWB_Writer("sag.nwb",
                               "sag",
                               "simulation of the Edyta's experiments")


  for key in holding_current.keys():
    
    if key.startswith("km"):
      if "ih" in key:
        a = key.index("ih")
        perc = float(key[2:a])
        cell.set_km(gmax_iM*perc, 50)
        perc = float(key[(a+2):])
        cell.set_h(gmax_iH*perc)
      else:
        perc = float(key[2:])
        cell.set_km(gmax_iM*perc, 50)
    elif key.startswith("ih"):
      perc = float(key[2:])
      cell.set_h(gmax_iH*perc)
      
    get_sag_curves(out, key, -0.05, -0.2, -0.05, holding_current[key])
    
    cell.set_km(gmax_iM, 50)
    cell.set_h(gmax_iH)

    
  out.close()
