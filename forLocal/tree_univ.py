from builtins import range
import math
from graphillion import GraphSet
import networkx as nx

# 0を根とする深さdで，深さiでの幅がn-iとなるようなtreeを与える
def tree_univ(n): #n=number of vertex
    m = n-1
    edges = []
    for k in range(n): #根からの辺
        edges.append((0, k))
    for i in range(m): #深さ
        for j in range(math.ceil((m-i)/2)): #右に辺が伸びる頂点
            for k in range(1, n-i-2*j-1): #辺
                #座標(i,j)の点はi(n-1)+j+1で与えられる
                edges.append((i*m+j+1, (i+1)*m+j+k)) 
    g = nx.Graph(edges)
    return g.edges()

def graph(g, universe=None):
    import matplotlib.pyplot as plt
    if not isinstance(g, nx.Graph):
        g = nx.Graph(list(g))
    if universe is None:
        universe = GraphSet.universe()
        #GraphSetクラスのuniverseタイプで要素が空のものとした．
    if not isinstance(universe, nx.Graph):
        universe = nx.Graph(list(universe))
    #ここまでで (g, universe) ともにnx.graphが定まった．
    
    n = len(g)
    m = n-1
    pos = {}
    #position: optional {'vartex':(x, y)}
    pos[0] = (-1, 0)
    for v in range(1, m**2):
        pos[v] = ((v-1) // m, (v-1) % m)
    nx.draw(g, pos)
    plt.show()

