# 重みづけしてイテレーションで同値類消したい
from graphillion import GraphSet
import graphillion.tutorial as tl 
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees

n = 8
wtd_tree = MakeUniverse().tu_wtd(n)
universe = wtd_tree[0]
wtd = wtd_tree[1]

g = [(0, 1), (0, 2), (0, 7), (1, 9), (1, 10), (9, 17), (10, 17)]

GraphSet.set_universe(universe)

draw = DrawGraph()
draw.graph(universe, n=8)
draw.graph(g, wtd, n=8)




'''
tree = GraphSet.trees(root=0, is_spanning=False)
gs = tree.len(8-1)
gs1 = gs.including(1)

subsets = tu.subsets(universe, gs)
subsets_list = [sorted(list(x)) for x in subsets]
tu.writelist(subsets_list, "test.txt")
'''


