from builtins import range
from graphillion import GraphSet

def tree_univ(d, w): #d=depth, w=width
    import networkx as nx
    edges = []
    for v in range(1, d * w + 2):
        if v <= w:
            edges.append((0, v))
        else:
            for u in range(1, w):
                edges.append((v, v - ((v-1) % w) - 1 - w + u))
    g = nx.Graph(edges)
    return g.edges()

def graph(g, universe=None):
    import networkx as nx
    import matplotlib.pyplot as plt
    if not isinstance(g, nx.Graph):
        g = nx.Graph(list(g))
    if universe is None:
        universe = GraphSet.universe()
    if not isinstance(universe, nx.Graph):
        universe = nx.Graph(list(universe))
    w = sorted(universe[1].keys())[1] - 1
    d = 1 + universe.number_of_nodes() // w
    g.add_nodes_from(universe.nodes())
    pos = {}
    pos[1] = (0, 0)
    for v in range(1, d * w + 2):
        pos[v] = (v % w, (d * w - v) // w)
    nx.draw(g, pos)
    plt.show()

