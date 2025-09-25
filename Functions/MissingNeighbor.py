import numpy as np
from BridgeBuilder import *
def MissingNeighbor(goneNodes,NodesCon):
    NextToNodesVec=NodesCon[1]        
    goneNodes_np=np.array(list(goneNodes))
    MissingBridgeLoc=NextToNodesVec==1
    MissingBridgeNodes=goneNodes_np[MissingBridgeLoc]
    if len(MissingBridgeNodes)>0:
        BridgeNodes=goneNodes_np[~MissingBridgeLoc]
        NodesCon=BridgeBuilder(BridgeNodes=BridgeNodes,
                               MissingBridgeNodes=MissingBridgeNodes,
                               goneNodes_np=goneNodes_np,
                               NodesCon=NodesCon)
        NodesCon=MissingNeighbor(goneNodes=goneNodes,
                                 NodesCon=NodesCon)
        
    return NodesCon
