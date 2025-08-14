import numpy as np
import networkx as nx
import math

def longest_path_in_tree(G):
    """2-pass BFS to get (u, v, path) of the tree diameter."""
    # first BFS
    s = next(iter(G.nodes))
    lengths = nx.single_source_shortest_path_length(G, s)
    u = max(lengths, key=lengths.get)
    # second BFS
    lengths = nx.single_source_shortest_path_length(G, u)
    v = max(lengths, key=lengths.get)
    path = nx.shortest_path(G, source=u, target=v)
    return u, v, path
