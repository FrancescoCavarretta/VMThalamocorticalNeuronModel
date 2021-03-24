from plots import Plot, VPlot
from pynwb import NWBHDF5IO
import numpy as np
import sag_analysis as SAG



 


  
class SAGplot(Plot):
  def __init__(self, ax, markersize=7.5, linewidth=2, markeredgecolor='black', markeredgewidth=2, labelsize=10, fontweight='normal'):
    super(SAGplot, self).__init__(ax,
      markersize=markersize,
      linewidth=linewidth,
      markeredgecolor=markeredgecolor,
      markeredgewidth=markeredgewidth,
      labelsize=labelsize,
      fontweight=fontweight,
      xlabel='Current (pA)',
      ylabel='SAG (%)',
      legend=True)
    
    self.ax.set_ylim([10,60])
    self.ax.set_xlim([-25,-225])
    self.ax.set_yticks(np.arange(20, 61, 20).tolist())
    self.ax.set_xticks(np.arange(-50, -201, -50).tolist())

  def _format_plot(self):
    super(SAGplot, self)._format_plot()
    self.ax.legend(prop={'weight' : self.fontweight, 'size' : self.labelsize}, loc=2, frameon=False, bbox_to_anchor=(0,1.15))



    


def plot_sag_curve(ax):
  io = NWBHDF5IO('sag.nwb', 'r')
  nwbfile = io.read()
  
  _sag_plot = SAGplot(ax)
  ii, ss = SAG.get_sag_curve(nwbfile, "control_%g", np.arange(0.05, 0.25, 0.05))
  _sag_plot.plot(-ii*1000, ss, color='black', label='Control')
  ii, ss = SAG.get_sag_curve(nwbfile, "km0_%g", np.arange(0.05, 0.25, 0.05))
  _sag_plot.plot(-ii*1000, ss, color='red', label='No K$_M$')
  ii, ss = SAG.get_sag_curve(nwbfile, "ih3_%g", np.arange(0.05, 0.25, 0.05))
  _sag_plot.plot(-ii*1000, ss, color='blue', label='300% I$_H$')
  ii, ss = SAG.get_sag_curve(nwbfile, "km0ih3_%g", np.arange(0.05, 0.25, 0.05))
  _sag_plot.plot(-ii*1000, ss, color='white', label='No K$_M$,300% I$_H$' )
  io.close()


  

def plot_vm_curve(ax, current=np.arange(0.05, 0.25, 0.05), stim_start=5000, stim_end=7000, xlim=[5000-50,7050], ylim=[-135,-65], key='control', color='black', title='Control'):
  io = NWBHDF5IO('sag.nwb', 'r')
  nwbfile = io.read()
  
  _sag_plot = VPlot(ax, title=title)
  _sag_plot.ax.set_ylim(ylim)
  for _current in current:
    trace = SAG.analysis.read_trace(nwbfile, "%s_%g" % (key, _current), stim_start=stim_start, stim_end=stim_end)
    _sag_plot.plot(trace['T'], trace['V'], xlim=xlim, color=color)


  io.close()


  
