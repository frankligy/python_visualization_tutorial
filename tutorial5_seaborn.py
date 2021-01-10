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

import seaborn as sns
import pandas as pd

# prepare datasets

penguin = sns.load_dataset('penguins')   # long form
synthesis = pd.DataFrame({'var1':data1,'var2':data2,'var3':data3})   # wideform
a = synthesis.stack().reset_index(-1)

# distribution plot

fig,ax = plt.subplots()
sns.histplot(data=penguin,kde=True,stat='frequency',x='bill_length_mm',hue='species',multiple='layer',
             kde_kws={'bw_adjust':5},line_kws={'linewidth':7},palette='Set2',ax=ax)
sns.rugplot(data=penguin,x='bill_length_mm',hue='species',ax=ax)
sns.histplot(data=synthesis,kde=True,stat='density',common_norm=False,hue_order=['var2','var1','var3'],
             multiple='layer')


sns.kdeplot(data=penguin,x='bill_length_mm',hue='species',clip=(35,100))
sns.rugplot(data=penguin,x='bill_length_mm',hue='species')



# categorical plot
sns.violinplot(data=penguin,x='species',y='bill_length_mm',hue='sex',split=True,bw=0.2,inner='quartile',scale_hue=True,
               scale='count')



sns.swarmplot(data=penguin,x='species',y='bill_length_mm',hue='sex',dodge=True)

sns.pointplot(data=penguin,x='species',y='bill_length_mm',hue='sex')

# regression plot
sns.regplot(data=penguin,x='bill_length_mm',y='bill_depth_mm')

# matrix plot
sns.heatmap(data=synthesis.iloc[0:5,:],annot=True,linewidths=0.5,square=True,yticklabels=False)
mask = np.array([[0,0,0],
         [0,0,0],
         [0,1,0],
         [0,0,0],
         [0,0,0]])
sns.heatmap(data=synthesis.iloc[0:5,:],annot=True,linewidths=0.5,square=True,yticklabels=False,mask=mask)


row_cb = pd.DataFrame(data=np.random.choice(['r','g','b','m'],(100,2)),index=np.arange(100),columns=['hey','ha'])
sns.clustermap(data=synthesis,row_colors=row_cb)


# pair plot and joint plot
sns.pairplot(data=penguin.iloc[:,[2,3,4,5]],dropna=True)
sns.jointplot(data=penguin,x='bill_length_mm',y='bill_depth_mm',kind='reg')


