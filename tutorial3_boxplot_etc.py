import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Arial'

import numpy as np

np.random.seed(42)
data1 = np.random.randn(100)
data2 = np.random.randn(100)
data3 = np.random.randn(100)

fig,ax = plt.subplots()
bp = ax.boxplot(x=[data1,data2,data3],positions=[1,5,7],patch_artist=True)
for flier in bp['fliers']:
    flier.set_markersize(9)
    flier.set_marker('v')
for box in bp['boxes']:
    box.set_facecolor('green')
    box.set_edgecolor('black')
    box.set_linewidth(2)
for whisker in bp['whiskers']:
    whisker.set_linewidth(5)
for cap in bp['caps']:
    cap.set_color('red')
    cap.set_linewidth(10)
for median in bp['medians']:
    median.set_linewidth(15)


fig,ax = plt.subplots()
ax.bar(x=[1,4,9],height=(data1.max(),data2.max(),data3.max()),width=0.5,edgecolor='black',color=['green','red','orange'],
       yerr=np.array([[0.1,0.1,0.1],[0.15,0.15,0.15]]),ecolor='red',capsize=5)


fig,ax = plt.subplots()
ax.hist(x=[data1,data2],bins=20,edgecolor='black')

fig,ax = plt.subplots()
ax.scatter(x=np.arange(10),y=np.arange(10)+5,s=np.arange(10)*10,c=np.random.rand(10),cmap='spring')
ax.scatter(x=[1,2,3],y=[1,2,3],s=[100,200,300],c=['r','g','b'])



fig,ax = plt.subplots()
ax.imshow(np.random.randn(5,5),cmap='Set1')
ax.set_xticks(np.linspace(0.5,3.5,4))
ax.set_yticks(np.linspace(0.5,3.5,4))
ax.tick_params(axis='both',length=0,labelsize=0)
ax.grid(b=True,which='major',axis='both',color='black')
ax.text(-0.2,3,'hey')





