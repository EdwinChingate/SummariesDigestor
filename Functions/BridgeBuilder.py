import numpy as np
from UpdateNodesConnectivity import *
def BridgeBuilder(BridgeNodes,MissingBridgeNodes,goneNodes_np,NodesCon):
    NodesConnectivity=NodesCon[0]
    NextToNodesVec=NodesCon[1]    
    for bridge_node in BridgeNodes:
        bridgeLoc=int(np.where(goneNodes_np==bridge_node)[0])
        nodeConnectivity=NodesConnectivity[bridgeLoc]
        node_attractor=nodeConnectivity[0]
        neighbors_attracted=nodeConnectivity[1]
        Neighbors=nodeConnectivity[2]
        missing_neighbors=set(Neighbors)&set(goneNodes_np)
        if len(missing_neighbors)>0:
            NodesCon=UpdateNodesConnectivity(missing_neighbors=missing_neighbors,
                                             bridgeLoc=bridgeLoc,
                                             NodesCon=NodesCon,
                                             goneNodes_np=goneNodes_np)
    return NodesCon
