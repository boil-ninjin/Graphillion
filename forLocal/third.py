from graphillion import GraphSet
import graphillion.tutorial as tl 
import tree_univ

universe = tree_univ.tree_univ(4, 16)
GraphSet.set_universe(universe)
tree_univ.graph(universe)

""" universe = tl.grid(3)
GraphSet.set_universe(universe)
tl.draw(universe) """

#tree = GraphSet.trees(root=1, is_spanning=False)
#gs = tree.len(4)
#tl.draw(gs.choice())

#tlじゃないやつだとろくに描画もできない
#tree_univ.graphでnetworkx.exception.NetworkXError: Node 0 has no positionとかでる．