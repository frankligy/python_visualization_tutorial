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

dataset = [data1,data2,data3]
positions = [1,5,7]
fig,ax = plt.subplots()
vp = ax.violinplot(dataset=dataset,positions=[1,5,7])

for body in vp['bodies']:
    body.set_facecolor('red')
    body.set_edgecolor('black')
    body.set_alpha(1)
vp['cmaxes'].set_color('black')
vp['cmins'].set_color('black')
vp['cbars'].set_color('black')

tmp = [np.percentile(data,[25,50,75]) for data in dataset]

def get_whisker(tmp,dataset):
    whisker = []
    for quantile,data in zip(tmp,dataset):
        data = np.array(data)
        q1 = quantile[0]
        median = quantile[1]
        q3 = quantile[2]
        iqr = q3 - q1
        upper = q3 + 1.5 * iqr
        upper = np.clip(upper,q3,data.max())
        lower = q1 - 1.5 * iqr
        lower = np.clip(lower,data.min(),q1)
        whisker.append((upper,lower))
    return whisker

whisker = get_whisker(tmp,dataset)
ax.scatter(positions,[quantile[1] for quantile in tmp],marker='o',color='white',s=30,zorder=3)
ax.vlines(positions,[quantile[0] for quantile in tmp],[quantile[2] for quantile in tmp],color='black',linestyle='-',lw=5)
ax.vlines(positions,[bound[0] for bound in whisker],[bound[1] for bound in whisker],color='black',linestyle='-',lw=4)


sample1 = np.random.randn(100)
sample2 = np.random.randn(100)
sample3 = np.random.randn(100)
sample4 = np.random.randn(100)
sample5 = np.random.randn(100)
sample6 = np.random.randn(100)

mat = np.row_stack([sample1,sample2,sample3,sample4,sample5,sample6])

from scipy.spatial.distance import pdist,squareform
dense_distance = pdist(mat,'euclidean')
square_distance = squareform(dense_distance)

from scipy.cluster.hierarchy import linkage,dendrogram
linkage_matrix = linkage(dense_distance,method='ward',metric='euclidean')
fig,ax = plt.subplots()
dendrogram(linkage_matrix,ax=ax)










