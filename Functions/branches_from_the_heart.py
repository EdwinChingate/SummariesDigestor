import numpy as np
import networkx as nx
def branches_from_the_heart(TreeSeed):
    betweenness_centrality=nx.betweenness_centrality(TreeSeed)
    top_nodes=np.array(sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:5])
    Heart=int(top_nodes[0])
    leaves = [n for n in TreeSeed.nodes() if TreeSeed.degree(n) == 1]
    Branches= [nx.shortest_path(TreeSeed, source=leaf, target=Heart) for leaf in leaves]
    Branches_and_Heart=[Branches,Heart]    
    return Branches_and_Heart
