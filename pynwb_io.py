import numpy as np

from datetime import datetime
from dateutil.tz import tzlocal
from pynwb import NWBFile
from pynwb.ecephys import ElectricalSeries
from pynwb import NWBHDF5IO


class My_NWB_Writer:
  def __init__(self, filename, name, description, session_id='MyHome'):
    self.io = NWBHDF5IO(filename, 'w')
    
    self.nwbfile = NWBFile(name,
                           name.replace(' ', '_'),
                           datetime.now(tzlocal()),
                           experimenter='Francesco Cavarretta',
                           lab='Jaeger lab',
                           institution='Emory University',
                           experiment_description=description,
                           session_id=session_id)
    
    self.device = self.nwbfile.create_device(name='ThalamicRelayCell')
    
    self.electrode_group = self.nwbfile.create_electrode_group('ThalamicRelayCell_000',
                                                               description="Thalamic Relay Cell somatic traces, Mouselight Morphologies",
                                                               location="VM Thalamus",
                                                               device=self.device)

    self.nwbfile.add_electrode(id=1,
                               imp=-1.0,
                               x=0.0,y=0.0,z=0.0,
                               location="VM Thalamus",
                               filtering='none',
                               group=self.electrode_group)

    self.electrode_table_region = self.nwbfile.create_electrode_table_region([0], 'an electrode')




  def write(self, name, t, v, description, comments=""):
    self.nwbfile.add_acquisition(ElectricalSeries(
      name, v, self.electrode_table_region, timestamps=t,
      resolution=0.001,
      comments=comments,
      description=description
      ))


  def close(self):
    self.io.write(self.nwbfile)
    self.io.close()
    
if __name__ == '__main__':
  out = My_NWB_Writer("sag.nwb", "sag", "Edyta's simulation")
  out.write("Control_%g_%g"%(abs(0), 2000.0), [1,2,3], [4,3,5], "2s hyperpolarizing current")
  out.close()
  
  io = NWBHDF5IO('sag.nwb', 'r')
  nwbfile = io.read()
  ephys_ts = nwbfile.acquisition['Control_0_2000']
  #elec2 = ephys_ts.electrodes[0]
  io.close()
