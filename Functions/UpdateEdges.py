from CheckEmptyFrames import *
from MissingNeighbor import *
from UpdateEdge import *
def UpdateEdges(goneNodes,WritingTree,CanvasDict,nodes_df,MaximumSimilarityTree):
    if len(goneNodes)==0:
        return CanvasDict   
    Heart=list(nodes_df["heart"])[0]
    NodesCon=CheckEmptyFrames(goneNodes=goneNodes,
                              WritingTree=WritingTree,
                              MaximumSimilarityTree=MaximumSimilarityTree,
                              Heart=Heart)        
    NodesCon=MissingNeighbor(goneNodes=goneNodes,
                             NodesCon=NodesCon)
    NodesConnectivity=NodesCon[0]
    for node_Connectivity in NodesConnectivity:
        node_attractor=node_Connectivity[0]
        neighbors_attracted=node_Connectivity[1]
        if len(neighbors_attracted)>0:
            CanvasDict=UpdateEdge(node_attractor=node_attractor,
                                  neighbors_attracted=neighbors_attracted,
                                  CanvasDict=CanvasDict,
                                  nodes_df=nodes_df)
    return CanvasDict
