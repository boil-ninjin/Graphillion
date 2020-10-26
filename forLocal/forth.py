from graphillion import GraphSet
import graphillion.tutorial as tl 
import tree_univ

universe = tree_univ.tree_univ(2, 4)
GraphSet.set_universe(universe)

tree = GraphSet.trees(root=0, is_spanning=False)
gs = tree.len(4)

print(len(gs))