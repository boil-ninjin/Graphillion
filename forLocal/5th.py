'''
tag class化以降で 互換性なくなった
具体的には
・関数をクラスに分けました
import tree_univ as tu
↓
from tree_univ import MakeUniverse, DrawGraph
・関数を統一しました
func graph とその一般化func graph_wtd があったが，前者を消して後者の名前をgraphとした．
'''








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