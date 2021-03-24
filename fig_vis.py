import fig_fi_curve_vis
import fig_rebound_vis
import fig_sag_vis


from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib
matplotlib.rc('pdf', fonttype=42)

import matplotlib.pyplot as plt


import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(8.27, 11.69), dpi=100, constrained_layout=True)
gs = gridspec.GridSpec(3, 2,
                       hspace=0.5,
                       wspace=0.3,
                       top=0.95,
                       bottom=0.05,
                       left=0.05,
                       right=0.95,
                       width_ratios=[2,1])


def plot_fi_curves():
  
  sub_gs_fi = gs[0, 0].subgridspec(1, 2, width_ratios=[1,1])
  
  fig_fi_curve_vis.plot_vm_curve(
    fig.add_subplot(
      sub_gs_fi[0, 0]
    ),
    key='control',
    color='black',
    title='Control'
  )
  
  fig_fi_curve_vis.plot_vm_curve(
    fig.add_subplot(
      sub_gs_fi[0, 1]
    ),
    key='km0',
    color='red',
    title='No I$_M$'
  )
    
  fig_fi_curve_vis.plot_fi_curve(
    fig.add_subplot(
      gs[0, 1]
    )
  )




def plot_rebound_curves():

  ## --------------------- traces ------------------------------ ##
  def get_inset_trace(_sub_gs_traces):
    return _sub_gs_traces.subgridspec(1, 2, width_ratios=[1, 2])

  
  sub_gs_traces = gs[1, 0].subgridspec(1, 2, width_ratios=[1,1])


  sub_gs_traces_control = get_inset_trace(sub_gs_traces[0, 0])
  fig_rebound_vis.plot_vm_curve(
    fig.add_subplot(
      sub_gs_traces_control[0, 1]
    ),
    0.1,
    highlight=(500, 5525, 5675, 'green'),
    title='Control',
    xlim=[4900, 7500]
  )

  fig_rebound_vis.plot_vm_curve(
    fig.add_subplot(
      sub_gs_traces_control[0, 0]
    ),
    0.1,
    key='control',
    color='green',
    durs=[500],
    xlim=[5525, 5675]
  )

  
  sub_gs_traces_nokm = get_inset_trace(sub_gs_traces[0, 1])
  fig_rebound_vis.plot_vm_curve(
    fig.add_subplot(
      sub_gs_traces_nokm[0, 1]
    ),
    0.1,
    key='km0',
    color='red',
    highlight=(500, 5525, 5675, 'purple'),
    title='No I$_M$',
    xlim=[4900, 7500]
  )
  
  fig_rebound_vis.plot_vm_curve(
    fig.add_subplot(
      sub_gs_traces_nokm[0, 0]
    ),
    0.1,
    key='km0',
    color='purple',
    durs=[500],
    xlim=[5525, 5675],
  )  


  sub_gs_spk = gs[1, 1].subgridspec(3, 1, height_ratios=[1,1,1])
  
  fig_rebound_vis.plot_spk_hist(
    fig.add_subplot(
      sub_gs_spk[0, 0]
    ),
    200,
    shift=-1,
    multiplier=4,
    key='control',
    color='black',
    xlabel=False,
    xticks=False,
    label='Control'
  )

  fig_rebound_vis.plot_spk_hist(
    fig.add_subplot(
      sub_gs_spk[0, 0]
    ),
    200,
    shift=0,
    multiplier=4,
    key='km0.5',
    color='pink',
    xlabel=False,
    xticks=False,
    label='50% I$_M$'
  )
  
  fig_rebound_vis.plot_spk_hist(
    fig.add_subplot(
      sub_gs_spk[0, 0]
    ),
    200,
    shift=1,
    multiplier=4,
    key='km0',
    color='red',
    xlabel=False,
    xticks=False,
    label='No I$_M$'
  )
  
  fig_rebound_vis.plot_spk_hist(
    fig.add_subplot(
      sub_gs_spk[1, 0]
    ),
    500,
    shift=-1,
    multiplier=4,
    key='control',
    color='black',
    xlabel=False,
    xticks=False
  )

  fig_rebound_vis.plot_spk_hist(
    fig.add_subplot(
      sub_gs_spk[2, 0]
    ),
    2000,
    shift=-1,
    multiplier=4,
    key='control',
    color='black'
  )
  

  
  fig_rebound_vis.plot_spk_hist(
    fig.add_subplot(
      sub_gs_spk[1, 0]
    ),
    500,
    shift=0,
    multiplier=4,
    key='km0.5',
    color='pink',
    xlabel=False,
    xticks=False
  )

  fig_rebound_vis.plot_spk_hist(
    fig.add_subplot(
      sub_gs_spk[2, 0]
    ),
    2000,
    shift=0,
    multiplier=4,
    key='km0.5',
    color='pink'
  )

  
  fig_rebound_vis.plot_spk_hist(
    fig.add_subplot(
      sub_gs_spk[1, 0]
    ),
    500,
    shift=1,
    multiplier=4,
    key='km0',
    color='red',
    xlabel=False,
    xticks=False
  )

  fig_rebound_vis.plot_spk_hist(
    fig.add_subplot(
      sub_gs_spk[2, 0]
    ),
    2000,
    shift=1,
    multiplier=4,
    key='km0',
    color='red'
  )
  

def plot_sag_curves():
  
  sub_gs_sag_vm = gs[2, 0].subgridspec(1, 3, width_ratios=[1,1,1])
  
  fig_sag_vis.plot_vm_curve(
    fig.add_subplot(
      sub_gs_sag_vm[0, 0]
    ),
    key='control',
    color='black',
    title='Control'
  )
  
  fig_sag_vis.plot_vm_curve(
    fig.add_subplot(
      sub_gs_sag_vm[0, 1]
    ),
    key='km0',
    color='red',
    title='No I$_M$'
  )
    
  fig_sag_vis.plot_vm_curve(
    fig.add_subplot(
      sub_gs_sag_vm[0, 2]
    ),
    key='ih3',
    color='blue',
    title='300% I$_H$'
  )


  fig_sag_vis.plot_sag_curve(
    fig.add_subplot(
      gs[2, 1]
    )
  )

  


plot_fi_curves()
plot_rebound_curves()
plot_sag_curves()


fig.text(3, 3, 'a', fontsize=12, fontweight='normal')
fig.text(3, 3, 'b', fontsize=12, fontweight='normal')
fig.text(3, 3, 'c', fontsize=12, fontweight='normal')

fig.text(0, 3/3.0, 'A', ha='left', va='top', fontweight='bold')
fig.text(2/3.0*0.925, 3/3.0, 'B', ha='left', va='top', fontweight='bold')
fig.text(0, 2/3.0, 'C', ha='left', va='top', fontweight='bold')
fig.text(2/3.0*0.925, 2/3.0, 'D', ha='left', va='top', fontweight='bold')
fig.text(0, 1/3.0, 'E', ha='left', va='top', fontweight='bold')
fig.text(2/3.0*0.925, 1/3.0, 'F', ha='left', va='top', fontweight='bold')


plt.show()
