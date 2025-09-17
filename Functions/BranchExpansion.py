import numpy as np

def BranchExpansion(node,LeavesPathwayMatrix):
    leaves=np.where(LeavesPathwayMatrix[:,node]>0)[0]
    LeavesDegree=LeavesPathwayMatrix[leaves,node]
    minL=int(min(LeavesDegree))
    maxL=int(max(LeavesDegree))
    NBranches=len(LeavesDegree)
    return [minL,maxL,NBranches]
