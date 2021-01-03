import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator
import numpy as np
import pandas as pd

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Arial'

np.random.seed(42)


x = np.arange(1,11,1)
y1 = np.linspace(300,400,10)
y2 = np.random.randint(low=300,high=400,size=10)

mpl.rcParams['lines.marker']  #None
mpl.rcParams['lines.markersize']  #6.0
mpl.rcParams['lines.linewidth']   # 1.5
mpl.rcParams['axes.prop_cycle']

mpl.colors.to_rgb('#1f77b4')

fig = plt.figure(figsize=(10,6))
ax = fig.add_axes([0.1,0.1,0.5,0.8])
p1 = ax.plot(x,y1,marker='o',markersize=8,markerfacecolor='red',markeredgecolor='black',markeredgewidth=2,
        linestyle='--',linewidth=3,zorder=3)
p2 = ax.plot(x,y2,marker='o')
ax.legend(handles=[p1[0],p2[0]],labels=['blue line','orange line'],loc='upper left',bbox_to_anchor=(1,1),
          title='legend',frameon=False)



