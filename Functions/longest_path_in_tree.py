import networkx as nx
def longest_path_in_tree(G):
    # First BFS
    u = list(G.nodes())[0]
    lengths = nx.single_source_shortest_path_length(G, u)
    farthest = max(lengths, key=lengths.get)
    
    # Second BFS from farthest node
    lengths = nx.single_source_shortest_path_length(G, farthest)
    other_end = max(lengths, key=lengths.get)
    
    # Get the actual path
    path = nx.shortest_path(G, source=farthest, target=other_end)
    return path

