# 重みづけしてイテレーションで同値類消したい
from graphillion import GraphSet
import graphillion.tutorial as tl 
import tree_univ as tu

n = 8
rtn = tu.tu_wtd(n)
universe = rtn[0]
wtd = rtn[1]
GraphSet.set_universe(universe)

tu.graph_wtd(universe, wtd, 8, universe=universe)

'''
tree = GraphSet.trees(root=0, is_spanning=False)
gs = tree.len(8-1)
gs1 = gs.including(1)

subsets = tu.subsets(universe, gs)
subsets_list = [sorted(list(x)) for x in subsets]
tu.writelist(subsets_list, "test.txt")
'''


