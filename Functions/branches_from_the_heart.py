import numpy as np
import networkx as nx
from operator import itemgetter
def branches_from_the_heart(Tree,MaximumSimilarityTree='',Heart=-1):
    if Heart<0:
        betweenness_centrality=nx.betweenness_centrality(Tree)
        top_nodes=np.array(sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:5])
        Heart=int(top_nodes[0])
    leaves=set([n for n in Tree.nodes() if Tree.degree(n) == 1])
    Branches= [nx.shortest_path(Tree, source=leaf, target=Heart) for leaf in leaves]
    nodes=np.array(Tree.nodes,dtype='int')
    if type(MaximumSimilarityTree)!=type('str'):
        NodesDegreeFullTree=np.array(itemgetter(*nodes)(MaximumSimilarityTree.degree))
        LeavesSetLoc=np.where(NodesDegreeFullTree!=2)[0]
        LeavesSet=set(nodes[LeavesSetLoc].tolist())    
        Leaves=np.array(list((LeavesSet|leaves)-set([Heart])))
    else:
        Leaves=np.array(list(leaves))
    Branches_Heart_and_Leaves=[Branches,Heart,Leaves]    
    return Branches_Heart_and_Leaves
