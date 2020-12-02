from graphillion import GraphSet
import graphillion.tutorial as tl  # チュートリアルのためのヘルパー・モジュール

'''
universe = tl.grid(8, 8)
GraphSet.set_universe(universe)
tl.draw(universe)  # ユニバースをポップアップウィンドウで表示する
'''

import networkx as nx
import matplotlib.pyplot as plt

# memo.mdの「Graphillonについて」の検証
universe = [(1, 2), (1, 4), (1, 3), (2, 5), (3, 6), (4, 5), (5, 6)]
#GraphSet.set_universe(universe)
universe = nx.Graph(list(universe))
print(universe[1])
print(list(universe[1].keys()))


#n = sorted(universe[1].keys())[1] 
#print(n)