# イテレーションを導入することで同値なグラフを代表元のみにする．
from graphillion import GraphSet
import graphillion.tutorial as tl 
import networkx as nx
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees

n = 8
[wtd_tree, wtd] = MakeUniverse().tu_wtd(n)

# universe内の頂点8の木がなすGraphsetを作る
# is_spanning はTrue にするとグラフセット全体ですべての頂点を通るようにしてくれる．
GraphSet.set_universe(wtd_tree)
tree = GraphSet.trees(root=0, is_spanning=False)
gs = tree.len(n-1)

'''
# 適当に制約を付けてchoice() で一つ選ぶ
gs1 = gs.including((1, 9))
g = gs1.choice()

draw = DrawGraph()
draw.graph(g, wtd, n=8)
'''

for k in range(8-1):
    [edge_k, wtd_k] = MakeUniverse().te_wtd(8, k)

    print(len(edge_k))
    draw = DrawGraph()
    draw.graph(edge_k, wtd_k, n=8)


