import numpy as np
from neighbour_in_branch import *
def branches_from_the_heart(TreeSeed):
    DegreeArray=np.array(TreeSeed.degree,dtype='int')
    LeavesLoc=np.where(DegreeArray[:,1]==1)[0]
    HeartLoc=np.where(DegreeArray[:,1]==len(LeavesLoc))[0]
    LeavesList=DegreeArray[LeavesLoc,0]
    Heart=int(DegreeArray[HeartLoc,0][0])
    EdgesArray=np.array(TreeSeed.edges)
    Branches=[]
    for leave in LeavesList:
        BranchList=[int(leave)]
        BranchList=neighbour_in_branch(BranchList=BranchList,
                                       EdgesArray=EdgesArray,
                                       Heart=Heart)
        Branches.append(BranchList)
    Branches_and_Heart=[Branches,Heart]
    return Branches_and_Heart
