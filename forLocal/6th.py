# list化すれば表示できるようになった！
# 重みづけすればイテレーションで同値類消せる気がするから7thで検証する
from graphillion import GraphSet
import graphillion.tutorial as tl 
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees


# リストを成分ごとに改行してファイルに書き込み
def writelist(list, path):
    strize = [str(x) for x in list]
    linebreak = "\n".join(strize)
    with open(path, mode='w') as f:
        f.write(str(linebreak))


n = 8
universe = MakeUniverse().tree_univ(n)
GraphSet.set_universe(universe)
# draw1 = Drawgraph()
# draw1.graph_wtd(universe, 8, universe=universe)

tree = GraphSet.trees(root=0, is_spanning=False)
gs = tree.len(8-1)
gs = gs.including(1)

print(type(gs))

subsets = OperationtoTrees().subsets(universe, gs)
subsets_list = [sorted(list(x)) for x in subsets]
writelist(subsets_list, "test.txt")
