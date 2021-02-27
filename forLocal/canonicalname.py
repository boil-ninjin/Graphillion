from graphillion import GraphSet
import graphillion.tutorial as tl 
import networkx as nx
import copy 
from tree_univ import MakeUniverse, DrawGraph, OperationtoTrees

class CanonicalName:
    # g はnx.Graphにしてくれ
    # 葉を特定する
    def leaf(self, G):
        leaf = [k for k in G if nx.degree(G)[k] == 1 and k != 0]
        return leaf

    # ある頂点を根とする（そこから上は無視する）部分木をとる
    # 方法は指定した頂点から上にある辺をすべて取り除いたのち
    # その頂点を含む連結成分をとっている
    def subtree(self, G, k):
        H = copy.deepcopy(G)
        path_to_parent = [(j, k) for j in H if G.has_edge(j, k) and j <= k]
        H.remove_edges_from(path_to_parent)
        conn_comp = nx.connected_components(H)
        node = list(filter(lambda x: k in x, conn_comp))[0]
        node_sorted = sorted(node)
        subtree = nx.induced_subgraph(H, node_sorted)
        return subtree

    # 再帰関数(頂点k を根とする木Gの個有名)
    def recuring(self, G, k):
        if k in self.leaf(G):
            return "(0)"
        
        subtree = self.subtree(G, k)
        neighbors = [i for i in subtree if subtree.has_edge(k, i)] # kとつながっている頂点
        children = [self.recuring(G, i) for i in neighbors] # 各nb.の個有名
        str_children = [str(a) for a in children]
        str_name = "".join(str_children)
        return "(" + str_name + ")"
    
    # 個有名
    def naming(self, G):
        return self.recuring(G, 0)


