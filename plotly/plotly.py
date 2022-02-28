import networkx as nx
import pandas as pd

# convert pandas edgelist or adjancencym matrix to network graph object
df1 = pd.DataFrame({'source':['node1','node1','node2'],'target':['node2','node3','node3'],'weight':[4.5,4.5,4.5],
                    'color':['blue','green','blue']}). # edge list
df2 = pd.DataFrame(data=[[0,4.5,4.5],[0,0,4.5],[0,0,0]],index=['node1','node2','node3'],columns=['node1','node2','node3']) # adjacency
G1 = nx.from_pandas_edgelist(df1,source='source',target='target',edge_attr='weight',create_using=nx.Graph)
G2 = nx.from_pandas_adjacency(df2,create_using=nx.Graph)

# nodes anatomy
type(G1.nodes())
# networkx.classes.reportviews.NodeView
list(G1.nodes())
# ['node1', 'node2', 'node3']
type(G1.nodes(data=True))
# networkx.classes.reportviews.NodeDataView
list(G1.nodes(data=True))
# [('node1', {}), ('node2', {}), ('node3', {})]
G1.nodes['node1']
# {}


# edges anatomy
type(G1.edges())
# networkx.classes.reportviews.EdgeView
list(G1.edges())
# [('node1', 'node2'), ('node1', 'node3'), ('node2', 'node3')]
type(G1.edges(data=True))
# networkx.classes.reportviews.EdgeDataView
list(G1.edges(data=True))
# [('node1', 'node2', {'weight': 4.5}),
# ('node1', 'node3', {'weight': 4.5}),
# ('node2', 'node3', {'weight': 4.5})]
G1.edges[('node1','node2')]
# {'weight': 4.5}


# set and get attributes
## node
node_color_dict = {'node1':'green','node2':'blue','node3':'red'}
nx.set_node_attributes(G1,node_color_dict,'color')
list(G1.nodes(data=True))
# [('node1', {'color': 'green'}),
# ('node2', {'color': 'blue'}),
# ('node3', {'color': 'red'})]
## edge 
nx.get_edge_attributes(G1,'weight')
# {('node1', 'node2'): 4.5, ('node1', 'node3'): 4.5, ('node2', 'node3'): 4.5}


import plotly.graph_objects as go
## step1: compute the graph layout (coordinates of nodes in 2D)
coords_dict = nx.spring_layout(G1,seed=42)
# {'node1': array([-0.33486468,  0.96136632]),
# 'node2': array([ 1.        , -0.19068184]),
# 'node3': array([-0.66513532, -0.77068448])}
## step2: set the dictionary as the attribute of the node
nx.set_node_attributes(G1,coords_dict,'coord')
## step3: validate
G1.nodes['node1']
#{'color': 'green', 'coord': array([-0.33486468,  0.96136632])}


node_x = []   # store x coordinates
node_y = []   # store y coordinates
node_text = [] # store text when mouse hovers over the node
for node,node_attr_dict in G1.nodes(data=True):  # recall anatomy 
    x,y = node_attr_dict['coord']
    node_x.append(x)
    node_y.append(y)
    node_text.append(node)
node_trace = go.Scatter(name='nodes',x=node_x,y=node_y,mode='markers',hoverinfo='text',text=node_text,marker={'color':'green','size':5})

edge_x = []
edge_y = []
for edge_end1,edge_end2,edge_attr_dict in G1.edges(data=True):
    x0,y0 = G1.nodes[edge_end1]['coord']
    x1,y1 = G1.nodes[edge_end2]['coord']
    x2,y2 = None,None
    for x,y in zip([x0,x1,x2],[y0,y1,y2]):
        edge_x.append(x)
        edge_y.append(y)
edge_trace = go.Scatter(name='lines',x=edge_x,y=edge_y,mode='lines',line=go.scatter.Line(color='black',width=2))


fig_layout = go.Layout(showlegend=True,title='network',xaxis=dict(title_text='coordinate x'))
fig = go.Figure(data=[node_trace,edge_trace],layout=fig_layout)
fig.write_html('./network.html',include_plotlyjs='cdn')


