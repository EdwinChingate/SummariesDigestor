import numpy as np
def UpdateNodesConnectivity(missing_neighbors,bridgeLoc,NodesCon,goneNodes_np):
    NodesConnectivity=NodesCon[0]
    NextToNodesVec=NodesCon[1]        
    for missing_neighbor in missing_neighbors:
        missing_neighborLoc=int(np.where(goneNodes_np==missing_neighbor)[0])
        NodesConnectivity[missing_neighborLoc][1]=NodesConnectivity[bridgeLoc][1]+NodesConnectivity[missing_neighborLoc][1]
        NodesConnectivity[missing_neighborLoc][0]=NodesConnectivity[bridgeLoc][0]
        NextToNodesVec[missing_neighborLoc]=0
    NodesCon=[NodesConnectivity,NextToNodesVec]
    return NodesCon
