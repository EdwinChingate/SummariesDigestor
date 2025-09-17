import numpy as np
from branches_from_the_heart import *

def LeavesPathway(MaximumSimilarityTree,Heart):
    Branches_Heart_and_Leaves=branches_from_the_heart(Tree=MaximumSimilarityTree,
                                                      MaximumSimilarityTree='',
                                                      Heart=Heart)
    Branches=Branches_Heart_and_Leaves[0]
    Nnodes=len(MaximumSimilarityTree.nodes)
    LeavesPathwayMatrix=np.zeros((Nnodes,Nnodes))
    for branch in Branches:
        leaf=branch[0]
        BranchLenght=len(branch)
        LeavesPathwayMatrix[leaf,branch]=np.arange(BranchLenght,dtype='int')+1
    return LeavesPathwayMatrix
