import numpy as np

def Branches_from_node(node,LeavesPathwayMatrix):
    Branches=[]
    Leaves_to_Node=np.where(LeavesPathwayMatrix[:,node]==1)[0]
    for leave in Leaves_to_Node:
        Branch=np.where(LeavesPathwayMatrix[leave,:]==1)[0]
        Branches.append(Branch)
    return Branches
