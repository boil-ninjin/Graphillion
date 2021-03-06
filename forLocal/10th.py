from graphillion import GraphSet
import networkx as nx
from tree_univ import ChangeCoordandSerial,MakeUniverse, DrawGraph, OperationtoTrees

n = 8
[wtd_tree, wtd] = MakeUniverse().tu_wtd(n)
GraphSet.set_universe(wtd_tree)

g = [(0, 1), (0, 2), (0, 3), (1, 8), (1, 9), (8, 15), (9, 16)]
h = [((-1, 0), (0, 0)), ((-1, 0), (0, 3)), ((0, 0), (1, 0)), ((0, 0), (1, 2)), ((4, 1), (5, 1))] 

c = ChangeCoordandSerial()
draw = DrawGraph()
cg = c.SerialtoCoord(g)
sh = c.CoordtoSerial(h, 8)

print(cg)
print(c.CoordtoSerial(cg))

print(sh)
print(c.SerialtoCoord(sh, 8))

draw.graph(g, n=8)
draw.graph(sh, n=8)
