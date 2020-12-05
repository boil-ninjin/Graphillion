from builtins import range
import math
from graphillion import GraphSet
import networkx as nx

# 0を根とする深さdで，深さiでの幅がn-iとなるようなtreeを与える
def tree_univ(n): #n=number of vertex
    m = n-1
    edges = []
    for k in range(1, n): #根からの辺
        edges.append((0, k))
    for i in range(m): #深さ
        for j in range(math.ceil((m-i)/2)): #右に辺が伸びる頂点
            for k in range(1, n-i-2*j-1): #辺
                #座標(i,j)の点はi(n-1)+j+1で与えられる
                edges.append((i*m+j+1, (i+1)*m+j+k)) 
    g = nx.Graph(edges)
    return g.edges()

# 上のtreeの重みづけ
def tu_wtd(n): #n=number of vertex
    m = n-1
    G = nx.Graph()
    edge = []
    for k in range(1, n): #根からの辺
        edge.append((0, k, k))
    for i in range(m): #深さ
        for j in range(math.ceil((m-i)/2)): #右に辺が伸びる頂点
            for k in range(1, n-i-2*j-1): #辺
                #座標(i,j)の点はi(n-1)+j+1で与えられる
                edge.append((i*m+j+1, (i+1)*m+j+k, k))
    G = G.add_weighted_edges_from(edge)
    edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
    return G, edge_labels

def set_univ(n):
    universe = tree_univ(n)
    GraphSet.set_universe(universe)

# 頂点nを含むgraph全体がなすsubGraphSetを第n成分とするリストを作る
def subsets(univ, gs):
    subsets = [univ, gs]
    for a in range(2, 8):
        subsets.append(gs.including(a))
        for b in range(2, a):
            subsets[a] = subsets[a].including(b)
    return subsets

# リストを成分ごとに改行してファイルに書き込み
def writelist(list, path):
    strize = [str(x) for x in list]
    linebreak = "\n".join(strize)
    with open(path, mode='w') as f:
        f.write(str(linebreak))


# 頂点数nのグラフを表示する．
# universeを表示したいときはnに各グラフの頂点数を入れること
def graph(g, n=None, universe=None):
    import matplotlib.pyplot as plt
    if not isinstance(g, nx.Graph):
        g = nx.Graph(list(g))
    if n is None:
        n = len(g)
    if universe is None:
        universe = GraphSet.universe()
        #GraphSetクラスのuniverseタイプで要素が空のものとした．
    if not isinstance(universe, nx.Graph):
        universe = nx.Graph(list(universe))
    #ここまでで (g, universe) ともにnx.graphが定まった．
    
    m = n-1
    pos = {}
    #position: optional {'vartex':(x, y)}
    pos[0] = (-1, 0)
    for v in range(1, m**2):
        pos[v] = ((v-1) // m, (v-1) % m)
    nx.draw(g, pos)
    plt.show()

def graph_wtd(g, wtd, n=None, universe=None):
    import matplotlib.pyplot as plt
    if n is None:
        n = len(g)
    if universe is None:
        universe = GraphSet.universe()
        #GraphSetクラスのuniverseタイプで要素が空のものとした．
    if not isinstance(universe, nx.Graph):
        universe = nx.Graph(list(universe))
    #ここまでで (g, universe) ともにnx.graphが定まった．
    
    m = n-1
    pos = {}
    #position: optional {'vartex':(x, y)}
    pos[0] = (-1, 0)
    for v in range(1, m**2):
        pos[v] = ((v-1) // m, (v-1) % m)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=wtd)
    plt.show()


