from builtins import range
import math
from graphillion import GraphSet
import networkx as nx
import matplotlib.pyplot as plt


class ChangeCoordandSerial:
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


    # 通し番号 → 座標番号(頂点) # n は木の位数
    def Node_SerialtoCoord(self, g, n):
            # if not isinstance(g, nx.Graph):
            # g = nx.Graph(list(g))

        m = n-1
        gcoord = []
        for v in g:
            gcoord.append(((v-1) // m, (v-1) % m))
        gcoord[0] = (-1, 0)
        return gcoord # listで返します．


    # 座標番号 → 通し番号(辺)
    def CoordtoSerial(self, g, n=None): # 座標番号はlistで与えてください．
        if n is None:
            n = len(g) +1 # 辺をリストで与えるとその長さは"頂点-1"になってしまう．
        
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


    # 座標番号 → 通し番号(頂点) # n は木の位数
    def Node_CoordtoSerial(self, g, n): # 座標番号はlistで与えてください．       
        m = n-1
        gserial = []
        for node in g:
            sortnode = sorted(node)

            if sortnode == (-1, 0):
                gserial.append(0)
            else:
                gserial.append((sortnode[0]*m + sortnode[1] + 1))

        return gserial # listで返します．
