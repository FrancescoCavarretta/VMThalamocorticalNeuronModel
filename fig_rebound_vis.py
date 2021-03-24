from plots import Plot, VPlot
from pynwb import NWBHDF5IO
import rebound_analysis
import numpy as np




class Bar(Plot):
  def __init__(self, ax, markersize=7.5, linewidth=2, markeredgecolor='black', markeredgewidth=2, labelsize=10, fontweight='normal', xlabel='Hyperpolarized Voltage Deflection (mV)', ylabel='# AP'):
    super(Bar, self).__init__(ax,
      markersize=markersize,
      linewidth=linewidth,
      markeredgecolor=markeredgecolor,
      markeredgewidth=markeredgewidth,
      labelsize=labelsize,
      fontweight=fontweight,
      xlabel=xlabel,
      ylabel=ylabel,
      legend=True)
    
    self.ax.set_ylim([0,5])
    self.ax.set_xlim([-2,10])    
    self.ax.set_yticks(np.arange(1, 6, 2).tolist())
    self.ax.set_xticks(np.arange(0, 12, 4).tolist())

  def _format_plot(self):
    super(Bar, self)._format_plot()
    self.ax.legend(prop={'weight' : self.fontweight, 'size' : self.labelsize}, loc=2, frameon=False, bbox_to_anchor=(0,1.5))


    
  def plot(self, x, y, yerr, label='', color='black'): #, xlabels=[]):

    self.ax.bar(
      x,
      y,
      yerr=yerr,
      color=color,
      linewidth      =self.linewidth,
      edgecolor='black',
      width=1,
      label=label
    )
    #self.ax.set_xticks([0,4,8])
    #self.ax.set_xticklabels(['0-20','40-60','60-80'])
    self._format_plot()


    


def plot_vm_curve(ax, current, stim_start=5000, stim_end=7000, xlim=[5000-100, 7500], key='control', color='black', highlight=None, durs=[200,500,2000], title=''):
  io = NWBHDF5IO('rebound.nwb', 'r')
  nwbfile = io.read()
  
  _rb_plot = VPlot(ax)
  _rb_plot.ax.set_ylim([-110,30])
  _rb_plot.ax.set_title(title, fontsize=10, fontweight='normal', loc='left')
  for dur in durs:
    trace = rebound_analysis.analysis.read_trace(nwbfile, "%s_%g_%g" % (key, current, dur), stim_start=stim_start, stim_end=stim_end)
    _rb_plot.plot(trace['T'], trace['V'], xlim=xlim, color=color)

  if highlight:
    dur, t_init, t_end, color = highlight
    trace = rebound_analysis.analysis.read_trace(nwbfile, "%s_%g_%g" % (key, current, dur), stim_start=stim_start, stim_end=stim_end)
    t = np.array(trace['T'])
    v = np.array(trace['V'])
    idx = np.logical_and(t >= t_init, t < t_end)
    t = t[idx]
    v = v[idx]
    _rb_plot.plot(t, v, color=color)
  io.close()



  
def plot_spk_hist(ax, dur, shift=0, multiplier=1, ii=np.arange(0.05, 0.55, 0.05), key='control', stim_start=7000, stim_end=7500, color='black', xlabel=True, xticks=True, label=''):
  io = NWBHDF5IO('rebound.nwb', 'r')
  nwbfile = io.read()

  # read the data
  hist = rebound_analysis.get_avg_spk(
    rebound_analysis.get_rebound_spk(
      nwbfile,
      key+"_%g",
      ii
    )
  )

  xlabels = []
  bb = Bar(ax, xlabel=('Hyperpolarized Voltage Deflection (mV)' if xlabel else ''))
  if not xticks:
    bb.ax.set_xticks([])
    
  xx = []
  yy = []
  yyerr = []
  for i, entry in enumerate(hist[dur].items()):

    dd = entry[0]
    
    mean = entry[1][0]
    std  = entry[1][1]

    xx.append(i*multiplier+shift)
    yy.append(mean)
    yyerr.append(std)

    xlabels.append('%g-%g'%(abs(dd[1]), abs(dd[0])))

  if xlabel:
    bb.ax.set_xticklabels(xlabels)
  bb.plot(xx, yy, yyerr, color=color, label=label)
  print (key)
  print ('\t',xx)
  print ('\t',yy)
  print ('\t',yyerr)
  io.close()  
