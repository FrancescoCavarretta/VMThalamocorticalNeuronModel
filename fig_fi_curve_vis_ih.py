from plots import Plot, VPlot
from pynwb import NWBHDF5IO
import fi_curve_analysis as FI
import numpy as np






class FIplot(Plot):
  def __init__(self, ax, markersize=7.5, linewidth=2, markeredgecolor='black', markeredgewidth=2, labelsize=10, fontweight='normal'):
    super(FIplot, self).__init__(ax,
      markersize=markersize,
      linewidth=linewidth,
      markeredgecolor=markeredgecolor,
      markeredgewidth=markeredgewidth,
      labelsize=labelsize,
      fontweight=fontweight,
      xlabel='Current (pA)',
      ylabel='Frequency (Hz)',
      legend=True)
    
    self.ax.set_ylim([-2.5, 30])
    self.ax.set_xlim([0,400])
    self.ax.set_yticks(np.arange(0, 31, 10).tolist())
    self.ax.set_xticks(np.arange(0, 401, 100).tolist())


    









  

  


  

  


    













def plot_fi_curve(ax, label=''):
  io = NWBHDF5IO('fi_curve.nwb', 'r')
  nwbfile = io.read()
  
  _fi_plot = FIplot(ax)
  ii, ff = FI.get_fi_curve(nwbfile, "control_%g", np.arange(0.03, 0.36, 0.01))
  _fi_plot.plot(ii*1000, ff, color='black', label='Control')
  ii, ff = FI.get_fi_curve(nwbfile, "ih2_%g", np.arange(0.03, 0.36, 0.01))
  _fi_plot.plot(ii*1000, ff, color='pink', label='+200% ih')
  ii, ff = FI.get_fi_curve(nwbfile, "ih3_%g", np.arange(0.03, 0.36, 0.01))
  _fi_plot.plot(ii*1000, ff, color='red', label='+300% ih')


  io.close()




def plot_vm_curve(ax, shift=0.05, stim_start=5000, stim_end=7000, xlim=[5000-50,5760], key='control', color='black', title=''):
  io = NWBHDF5IO('fi_curve.nwb', 'r')
  nwbfile = io.read()
  
  _fi_plot = VPlot(ax, title=title)
  
  _ii_rheobase_control = shift+FI.get_rheobase(
    *FI.get_fi_curve(nwbfile, "control_%g", np.arange(0.01, 0.36, 0.01))
  )
  
  trace = FI.analysis.read_trace(nwbfile, "%s_%g" % (key, _ii_rheobase_control), stim_start=stim_start, stim_end=stim_end)
  _fi_plot.plot(trace['T'], trace['V'], xlim=xlim, color=color)


  io.close()


  
