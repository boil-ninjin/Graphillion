# CanonicalName.py のテスト用

from graphillion import GraphSet
import graphillion.tutorial as tl 
import networkx as nx
from canonicalname import CanonicalName 
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees

n = 8
[wtd_tree, wtd] = MakeUniverse().tu_wtd(n)
GraphSet.set_universe(wtd_tree)

g = [(0, 1), (0, 2), (0, 3), (1, 8), (1, 9), (8, 15), (9, 16)]
h = [(0, 1), (1, 8), (8, 15), (15, 22), (22, 29), (29, 36), (36, 43)]
G1 = nx.Graph(g)
H1 = nx.Graph(h)

c = CanonicalName()
#print(c.leaf(G1))
print(c.leaf(H1))
print(c.recuring(G1, 1))
print(c.recuring(H1, 1))
print(c.naming(G1))
print(c.naming(H1))
draw = DrawGraph()
draw.graph(G1, wtd, n=8)
draw.graph(H1, wtd, n=8)
draw.graph(c.subtree(G1, 8), wtd, n=8)
draw.graph(c.subtree(H1, 0), wtd, n=8)
