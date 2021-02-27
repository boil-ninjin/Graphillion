from graphillion import GraphSet
import networkx as nx
import numpy as np
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees
from ChangeCoord import ChangeCoordandSerial
import csv

def writelist(list, path):
    strize = [str(x) for x in list]
    linebreak = "\n".join(strize)
    with open(path, mode='w') as f:
        f.write(str(linebreak))

def writecsv(array, path): # array は二次元配列
    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(array)


n = 8
[wtd_tree, wtd] = MakeUniverse().tu_wtd(n)
GraphSet.set_universe(wtd_tree)
edges = list(wtd_tree)
arrayedge = np.array(edges)

a = arrayedge
print(a)
print(len(a))
np.savetxt("tests/test.txt", a, fmt="%d")

# with open("tests/test.txt") as f:
#    print(f.read())

# print(np.loadtxt("tests/test.txt"))
print(len(np.loadtxt("tests/test.txt")))