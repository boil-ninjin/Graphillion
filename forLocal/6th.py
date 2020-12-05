# list化すれば表示できるようになった！
# 重みづけすればイテレーションで同値類消せる気がするから7thで検証する
from graphillion import GraphSet
import graphillion.tutorial as tl 
import tree_univ as tu

n = 8
tu.set_univ(n)
universe = GraphSet.universe()
#tu.graph_univ(universe, 8, universe=universe)

tree = GraphSet.trees(root=0, is_spanning=False)
gs = tree.len(8-1)
gs = gs.including(1)

print(type(gs))

subsets = tu.subsets(universe, gs)
subsets_list = [sorted(list(x)) for x in subsets]
tu.writelist(subsets_list, "test.txt")
