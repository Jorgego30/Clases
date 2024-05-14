import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os

df = pd.read_csv("Output.csv",sep=';')

froms = [df.loc[i]['f'] for i in range(df.shape[0])]
tos = [df.loc[i]['t'] for i in range(df.shape[0])]
weight = [df.loc[i]['w'] for i in range(df.shape[0])]

labels = {}
for i in range(df.shape[0]):
    clave = (froms[i],tos[i])
    valor = weight[i]
    labels[clave] = valor


G = nx.DiGraph()

for i in range(1,max(tos),1):
    G.add_node(i)

for i in range(df.shape[0]):
    G.add_edge(froms[i], tos[i], weight=weight[i])


pos = nx.circular_layout(G)
plt.figure()
nx.draw(
    G, pos, edge_color='black', width=1, linewidths=2,
    node_size=1500, node_color='skyblue', with_labels=True, font_size=12, arrows=True
)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=labels,
    font_color='black'
)
plt.axis('off')
plt.show()


try:
    os.remove("Output.csv")
    os.remove("OutputwCol.csv")
except:
    pass