import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator

a = pd.Series(list(mpl.rcParams.keys()))


mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Arial'

fig = plt.figure()
mpl.rcParams['figure.figsize']   # [6.4,4.8] 6.4 is the width, 4.8 is the height
fig = plt.figure(figsize=(10,6))
ax = plt.axes((0.1,0.1,0.5,0.8))
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(axis='x',which='major',direction='out',length=10,width=5,color='red',pad=15,labelsize=15,labelcolor='green',
               labelrotation=15)
ax.set_xticks([0.2,1])
ax.set_xticklabels(['pos1','pos2'])

ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

a=ax.yaxis.get_major_locator()
b=ax.yaxis.get_major_formatter()

ax.grid(True,which='major',axis='both',alpha=0.3)

c = ax.get_xticks()
d = ax.get_xticklabels()

fig,axes = plt.subplots(nrows=4,ncols=4,figsize=(10,6))
fig,axes = plt.subplots(nrows=4,ncols=4,figsize=(10,6),gridspec_kw={'wspace':0.5,'hspace':0.5})





