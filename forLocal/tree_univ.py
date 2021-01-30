from builtins import range
import math
from graphillion import GraphSet
import networkx as nx
import matplotlib.pyplot as plt


class ChangeCoordandSerial:
    # 通し番号 → 座標番号(頂点)
    def Node_SerialtoCoord(self, g, n=None):
            # if not isinstance(g, nx.Graph):
            # g = nx.Graph(list(g))
        if n is None:
            n = len(g)

        m = n-1
        gcoord = []
        for v in g:
            gcoord.append(((v-1) // m, (v-1) % m))
        gcoord[0] = (-1, 0)
        return gcoord # listで返します．


    # 通し番号 → 座標番号(辺)
    def SerialtoCoord(self, g, n=None):
        if not isinstance(g, nx.Graph):
            g = nx.Graph(list(g))
        if n is None:
            n = len(g)
        
        m = n-1
        gcoord = []
        for edge in g.edges():
            e = sorted(edge)
            if e[0] == 0:
                gcoord.append(((-1, 0), ((e[1]-1) // m, (e[1]-1) % m)))
            else:
                gcoord.append((((e[0]-1) // m, (e[0]-1) % m), ((e[1]-1) // m, (e[1]-1) % m)))
        gCoord = nx.Graph(gcoord)
        return gCoord.edges()


    # 座標番号 → 通し番号(辺)
    def CoordtoSerial(self, g, n=None): # 座標番号はlistで与えてください．
        if n is None:
            n = len(g)
        
        m = n-1
        gserial = []
        for edge in g:
            (i, j) = sorted((edge[0], edge[1]))

            if -1 in i:
                gserial.append((0, j[0]*m + j[1] + 1))
            else:
                gserial.append((i[0]*m + i[1] + 1, j[0]*m + j[1] + 1))
        gSerial = nx.Graph(gserial)
        return gSerial.edges()



class MakeUniverse:
    # 0を根とする深さdで，深さiでの幅がn-iとなるようなtreeを与える
    def tree_univ(self, n): #n=number of vertex
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
    def tu_wtd(self, n): #n=number of vertex
        m = n-1
        g = nx.Graph()
        edge = []
        for k in range(1, n): #根からの辺
            edge.append((0, k, [0, 0, k]))
        for i in range(m): #深さ
            for j in range(math.ceil((m-i)/2)): #右に辺が伸びる頂点
                for k in range(1, n-i-2*j-1): #辺
                    #座標(i,j)の点はi(n-1)+j+1で与えられる
                    edge.append((i*m+j+1, (i+1)*m+j+k, [i+1, j, k]))
        g.add_weighted_edges_from(edge)
        edge_labels = {(i, j): w['weight'] for i, j, w in g.edges(data=True)}
        return g.edges(), edge_labels


    # tree_univ の深さk から k+1 への辺のみがなす部分集合
    def tree_edge(self, n, i):
        m = n-1
        edges = []
        if i == 0:
            for k in range(1, n): #根からの辺
                edges.append((0, k))
        else: # もとのtree_univ ではi は0 から始まるのでi=i-1 とする
            i = i-1
            for j in range(math.ceil((m-i)/2)): #右に辺が伸びる頂点
                for k in range(1, n-i-2*j-1): #辺
                    #座標(i,j)の点はi(n-1)+j+1で与えられる
                    edges.append((i*m+j+1, (i+1)*m+j+k)) 
        g = nx.Graph(edges)
        return g.edges()


    # （必要あるかはわからんけど）上の重み付きver
    def te_wtd(self, n, i):
        m = n-1
        g = nx.Graph()
        edge = []
        if i == 0:
            for k in range(1, n): #根からの辺
                edge.append((0, k, [0, 0, k]))
        else: # もとのtree_univ ではi は0 から始まるのでi=i-1 とする
            i = i-1
            for j in range(math.ceil((m-i)/2)): #右に辺が伸びる頂点
                for k in range(1, n-i-2*j-1): #辺
                    #座標(i,j)の点はi(n-1)+j+1で与えられる
                    edge.append((i*m+j+1, (i+1)*m+j+k, [i+1, j, k]))
        g.add_weighted_edges_from(edge)
        edge_labels = {(i, j): w['weight'] for i, j, w in g.edges(data=True)}
        return g.edges(), edge_labels


class DrawGraph:
    # 頂点数nのグラフを表示する．
    # かつてあった関数”graph”の一般化
    def graph(self, g, wtd=None, n=None, universe=None):
        if not isinstance(g, nx.Graph):
            g = nx.Graph(list(g))
        if n is None:
            n = len(g)
        if universe is None:
            universe = GraphSet.universe()
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
        if wtd is None:
            pass
        else:
            label = {s: wtd[s] for s in g.edges()}
            nx.draw_networkx_edge_labels(g, pos, edge_labels=label)
        
        plt.show()


class OperationtoTrees:
    # 頂点nを含むgraph全体がなすsubGraphSetを作る
    def subset(self, gs, n, universe=None):
        if universe is None:
            universe = GraphSet.universe()
        return gs.including(n)  


    # 頂点nを含むgraph全体がなすsubGraphSetを第n成分とするリストを作る
    def subsets(self, univ, gs):
        subsets = [univ, gs]
        for a in range(2, 8):
            subsets.append(gs.including(a))
            for b in range(2, a):
                subsets[a] = subsets[a].including(b)
        return subsets



