from graphillion import GraphSet
import graphillion.tutorial as tl 
import networkx as nx
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees

class CanonicalName:
    # 葉を取る
    def leaf(self, g):
        leaf = [k for k in g if nx.degree(g)[k] == 1]
        return leaf


    # 木の同型類を与える
    def namingcan(g, n=None):
        if not isinstance(g, nx.Graph):
            g = nx.Graph(list(g))
        if n is None:
            n = len(g)

        m = n-1
        pos = {}
        #position: optional {'vartex':(x, y)}
        pos[0] = (-1, 0)
        for v in range(1, m**2):
            pos[v] = ((v-1) // m, (v-1) % m)

        for j in reversed(range(1, 8)):
            

        node_labels = {l: 10['value'] for l in leaf}
        chiledren = leaf
        for i in chiledren:
            j = g.neighbors[i][0]
            k = sum(k in g.neighbors[j] and k in children)


n = 8
[wtd_tree, wtd] = MakeUniverse().tu_wtd(n)
GraphSet.set_universe(wtd_tree)

g = [(0, 1), (0, 2), (0, 3), (1, 8), (1, 9), (8, 15), (9, 16)]
G = nx.Graph(g)

print(CanonicalName().leaf(G))
draw = DrawGraph()
draw.graph(G, wtd, n=8)

