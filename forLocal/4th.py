#根つき木をNetworkXで表示できるようになった．
from graphillion import GraphSet
import graphillion.tutorial as tl 
import tree_univ

universe = tree_univ.tree_univ(8)
GraphSet.set_universe(universe)

tree = GraphSet.trees(root=0, is_spanning=False)
gs = tree.len(8-1)
gs = gs.including(1)

print(len(gs))

tree_univ.graph(gs.choice(), universe=universe)
#tree_univ.graph_univ(universe, 8, universe=universe)
'''
# 頂点nを含むgraph全体がなすsubGraphSetを第n成分とするリスト
def subset():

subsets = [universe, gs]

for a in range(2, 8):
    subsets.append(gs.including(a))
    for b in range(2, a):
        subsets[a] = subsets[a].including(b)


subsets_map = map(str, subsets)
subsets_str = "\n".join(subsets_map)
filepath = "test.txt"
with open(filepath, mode='w') as f:
    f.write(str(subsets_str))

'''

