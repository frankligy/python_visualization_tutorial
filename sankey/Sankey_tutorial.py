
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Rectangle

# draw the canvas and ax
fig,ax = plt.subplots()
ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.grid()

# draw the recs
rec_left = Rectangle(xy=(0.1,0.6),width=0.2,height=0.2,facecolor='orange',edgecolor='k')
ax.add_patch(rec_left)
rec_right = Rectangle(xy=(0.7,0.2),width=0.2,height=0.2,facecolor='green',edgecolor='k')
ax.add_patch(rec_right)

# demo the path object logics
verts = [(0.3,0.8),(0.5,0.8),(0.7,0.4),(0.3,0.6),(0.3,0.8)]
codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
p = Path(verts,codes)
ax.add_patch(PathPatch(p,fc='none'))

# method1, Path, demo the curve4 logics
verts = [(0.3,0.8), (0.5,0.8), (0.5,0.4), (0.7,0.4)]
codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
p = Path(verts,codes)
ax.add_patch(PathPatch(p,fc='none',alpha=0.6))

# method1, path
verts = [(0.3,0.8), (0.5,0.8), (0.5,0.4), (0.7,0.4), (0.7,0.2), (0.5,0.2), (0.5,0.6), (0.3,0.6), (0.3,0.8)]
codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CLOSEPOLY]
p = Path(verts,codes)
ax.add_patch(PathPatch(p,fc='red',alpha=0.6))

# method2, convolve
yu = np.array(50*[0.8] + 50*[0.4])
yu_c = np.convolve(yu, 0.05*np.ones(20),mode='valid')
yu_cc = np.convolve(yu_c, 0.05*np.ones(20),mode='valid')
yd = np.array(50*[0.6] + 50*[0.2])
yd_c = np.convolve(yd, 0.05*np.ones(20),mode='valid')
yd_cc = np.convolve(yd_c, 0.05*np.ones(20),mode='valid')
ax.fill_between(np.linspace(0.3,0.7,62),yd_cc,yu_cc,color='blue',alpha=0.6)