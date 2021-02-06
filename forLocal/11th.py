from graphillion import GraphSet
import networkx as nx
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees
from ChangeCoord import ChangeCoordandSerial

def writelist(list, path):
    strize = [str(x) for x in list]
    linebreak = "\n".join(strize)
    with open(path, mode='w') as f:
        f.write(str(linebreak))



n = 8
[wtd_tree, wtd] = MakeUniverse().tu_wtd(n)
GraphSet.set_universe(wtd_tree)
edges = list(wtd_tree)
listoflist = []

for e in edges:
    E = [e]
    listoflist.append(E)

tree = GraphSet.trees(root=0, is_spanning=False)
gs = tree.len(n-1)
tr = list(gs)

writelist(tr, "edges.txt")
