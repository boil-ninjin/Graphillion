'''
tag class化以降で 互換性なくなった
具体的には
・関数をクラスに分けました
import tree_univ as tu
↓
from tree_univ import MakeUniverse, DrawGraph
・関数を統一しました
func graph とその一般化func graph_wtd があったが，前者を消して後者の名前をgraphとした．
'''









#4thの準備に手を動かしただけ
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