import numpy as np
import networkx as nx
def CheckEmptyFrames(goneNodes,WritingTree,MaximumSimilarityTree,Heart):
    nodes_writing_tree=set(WritingTree.nodes)    
    NodesConnectivity=[]
    N_goneNodes=len(goneNodes)
    NextToNodesVec=np.zeros(N_goneNodes)
    for gone in np.arange(N_goneNodes):
        node=list(goneNodes)[gone]
        Neighbors=set(list(MaximumSimilarityTree.neighbors(node)))
        path_to_the_heart=set(nx.shortest_path(MaximumSimilarityTree, source=node, target=Heart))
        neighbors_writing_tree=Neighbors&nodes_writing_tree
        neighbor_attractor=neighbors_writing_tree&path_to_the_heart
        if len(neighbor_attractor)>0:        
            node_attractor=list(neighbor_attractor)[0] 
        else:
            node_attractor=-1
            NextToNodesVec[gone]=1
        neighbors_attracted=list(neighbors_writing_tree-neighbor_attractor)    
        NodesConnectivity.append([node_attractor,neighbors_attracted,Neighbors,node])
    NodesCon=[NodesConnectivity,NextToNodesVec]
    return NodesCon
