import numpy as np
from LeavesPathway import *
def LeavesOneWay(MaximumSimilarityTree,Heart,Leaves):
    LeavesPathwayMatrix=LeavesPathway(MaximumSimilarityTree=MaximumSimilarityTree,
                                      Heart=Heart)      
    NRows=LeavesPathwayMatrix.shape[0]
    LeavesOnewayMatrix=np.zeros((NRows,NRows))
    for row in np.arange(NRows):
        PossibleLeaf=LeavesPathwayMatrix[row,Leaves].copy()
        SortLocPossibleLeaf=np.argsort(PossibleLeaf)
        SortPossibleLeaf=PossibleLeaf[SortLocPossibleLeaf]
        PositiveLoc=np.where(PossibleLeaf>0)[0]
        if len(PositiveLoc)>0:
            Leaves_in_Branch=PossibleLeaf[PositiveLoc]
            Closest_Leaf_Distance=min(Leaves_in_Branch)
            Closest_LeafLoc=np.where(Leaves_in_Branch==Closest_Leaf_Distance)[0]
            EntryLeaf=int(Leaves[PositiveLoc[Closest_LeafLoc]])
            DistanceEntryLeaf=int(Leaves_in_Branch[Closest_LeafLoc])
            LeavesOnewayMatrix[row,EntryLeaf]=DistanceEntryLeaf
    return LeavesOnewayMatrix
