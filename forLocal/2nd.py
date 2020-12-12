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









#チュートリアルの写経
from graphillion import GraphSet
import graphillion.tutorial as tl  # チュートリアルのためのヘルパー・モジュール


universe = tl.grid(8, 8)
GraphSet.set_universe(universe)
filepath = "test.txt"

print("good so far")

def cal(start, goal):
    paths = GraphSet.paths(start, goal)
    return len(paths)  
    # 結果が大規模のときは paths.len() を使う

n = cal(1, 81)
print(n)

with open(filepath, mode='w') as f:
    f.write(str(n))



