from graphillion import GraphSet
import graphillion.tutorial as tl 
import tree_univ

universe = tree_univ.tree_univ(8)
GraphSet.set_universe(universe)

#gs = [(0, 1), (0, 2), (1, 8), (1, 9), (2, 10), (8, 15), (15, 22)]


tree = GraphSet.trees(root=0, is_spanning=False)
gs = tree.len(8-1)
gs = gs.including(1)

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

print(len(gs))

tree_univ.graph(gs.choice(), universe=universe)
#tree_univ.graph(universe, universe=universe)
'''