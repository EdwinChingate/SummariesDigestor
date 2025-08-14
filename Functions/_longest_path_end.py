import networkx as nx

def _longest_path_end(G):
    s = next(iter(G.nodes))
    u = max(nx.single_source_shortest_path_length(G, s), key=lambda k: _)[0]  # first far end
    return u
