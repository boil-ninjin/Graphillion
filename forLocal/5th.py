from builtins import range
from graphillion import GraphSet
import networkx as nx
import matplotlib.pyplot as plt

# networkXの表示をする練習

g = [(0, 1), (0, 2), (1, 8), (1, 9), (2, 10), (8, 15), (15, 22)]
g = nx.Graph(list(g))
m = 7

pos = {}
#position: optional {'vartex':(x, y)}
pos[0] = (-1, 1)
pos[1] = (0, 1)
for v in range(1, m**2):
    pos[v] = (v // m, v % m)
nx.draw(g, pos)
plt.show()