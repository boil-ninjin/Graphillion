# 重みづけしてイテレーションで同値類消したい
# 関数を重みづけしたものに拡張した．
# 任意のグラフg をdrawできるようになった．
from graphillion import GraphSet
import graphillion.tutorial as tl 
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees

n = 8
wtd_tree = MakeUniverse().tu_wtd(n)
universe = wtd_tree[0]
wtd = wtd_tree[1]

g = [(0, 1), (0, 2), (0, 3), (1, 8), (1, 9), (8, 15), (9, 16)]

GraphSet.set_universe(universe)

draw = DrawGraph()
# draw.graph(universe, wtd, n=8)
draw.graph(g, wtd, n=8)




'''
subsets = tu.subsets(universe, gs)
subsets_list = [sorted(list(x)) for x in subsets]
tu.writelist(subsets_list, "test.txt")
'''


