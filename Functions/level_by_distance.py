import networkx as nx

def level_by_distance(G, root):
    """Return dict node->level using unweighted shortest path distance from root."""
    return nx.single_source_shortest_path_length(G, root)
