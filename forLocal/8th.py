#G.has_edge() を弄った．

from graphillion import GraphSet
import graphillion.tutorial as tl 
import networkx as nx
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees

n = 8
[wtd_tree, wtd] = MakeUniverse().tu_wtd(n)
GraphSet.set_universe(wtd_tree)

g = [(0, 1), (0, 2), (0, 3), (1, 8), (1, 9), (8, 15), (9, 16)]
G = nx.Graph(g)

# 与えられた辺がグラフに含まれているか判別する
x = (1, 4)
print(G.has_edge(*x)) # *はアンパック

# gに含まれている辺にTrue, 含まれていない辺にFalseを付けたKey=Value をメモ帳に送る
edgedistinct = {}
for k in range(n-1):
    edgedistinct |= {str(x) : G.has_edge(*x) for x in MakeUniverse().te_wtd(8, k)[0] }

filepath = "test.txt"
with open(filepath, mode='w') as f:
    f.write(str(edgedistinct))


# 深さk からk+1 への辺の総数を与える
EG0 = sum(G.has_edge(*x) for x in MakeUniverse().te_wtd(8, 0)[0])
EG1 = sum(G.has_edge(*x) for x in MakeUniverse().te_wtd(8, 1)[0])
EG2 = sum(G.has_edge(*x) for x in MakeUniverse().te_wtd(8, 2)[0])
EG3 = sum(G.has_edge(*x) for x in MakeUniverse().te_wtd(8, 3)[0])

print(EG0, EG1, EG2, EG3)


