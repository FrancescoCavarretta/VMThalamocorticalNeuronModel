class Plot:
  def __init__(self,
               ax,
               markersize=7.5,
               linewidth=2,
               markeredgecolor='black',
               markeredgewidth=2,
               labelsize=10,
               fontweight='normal',
               xlabel='',
               ylabel='',
               legend=True,
               title=''):
    self.ax         = ax
    self.markersize = markersize
    self.linewidth  = linewidth
    self.markeredgecolor = markeredgecolor
    self.markeredgewidth = markeredgewidth
    self.ax.spines['left'].set_linewidth(linewidth)
    self.ax.spines['right'].set_linewidth(0)
    self.ax.spines['top'].set_linewidth(0)
    self.ax.spines['bottom'].set_linewidth(linewidth)
    self.ax.tick_params(width=linewidth,labelsize=labelsize)
    self.ax.set_xlabel(xlabel,fontweight=fontweight, fontsize=labelsize)
    self.ax.set_ylabel(ylabel,fontweight=fontweight, fontsize=labelsize)
    self.fontweight = fontweight
    self.labelsize  = labelsize
    self.legend     = legend
    self.ax.set_title(title, fontsize=labelsize, fontweight=fontweight)



  def _format_plot(self):
    for label in (self.ax.get_xticklabels() + self.ax.get_yticklabels()):
      label.set_fontweight(self.fontweight)
    
    if self.legend:
      self.ax.legend(prop={'weight':self.fontweight, 'size':self.labelsize}, loc=2, frameon=False)


  def plot(self, x, y, label='', color='black'):
    self.ax.plot(x,
      y,
      '-ok',
      label          =label,
      color          ='black',
      markersize     =self.markersize,
      linewidth      =self.linewidth,
      markeredgecolor=self.markeredgecolor,
      markerfacecolor=color,
      markeredgewidth=self.markeredgewidth)

    
    self._format_plot()

    

class VPlot(Plot):
  def __init__(self, ax, linewidth=2, title=''):

    super(VPlot, self).__init__(ax,
      markersize=0,
      linewidth=0,
      markeredgecolor='black',
      markeredgewidth='black',
      labelsize=10,
      fontweight='normal',
      xlabel='',
      ylabel='',
      legend=False,
      title=title)

    self._plot_linewidth = linewidth
    self.ax.axes.xaxis.set_visible(False)
    self.ax.axes.yaxis.set_visible(False)
    self.ax.set_yticklabels([])
    self.ax.set_xticklabels([])
    self.ax.set_ylim([-80,30])



    
  def plot(self, x, y, xlim=None, color='black'):
    self.ax.plot(x,
      y,
      color          =color,
      linewidth      =self._plot_linewidth)


    if xlim:
      self.ax.set_xlim(xlim)
      
