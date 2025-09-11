import numpy as np
def neighbour_in_branch(BranchList,EdgesArray,Heart):
    node=BranchList[-1]    
    if node==Heart:        
        return BranchList
    NodeLoc=np.where(EdgesArray==node)
    NeighbourRow=int(NodeLoc[0])
    NeighbourCol=np.abs(NodeLoc[1]-1)
    Neighbour=int(EdgesArray[NeighbourRow,NeighbourCol][0])
    BranchList.append(Neighbour)
    EdgesArrayUpdated=np.delete(EdgesArray,NeighbourRow, axis=0)
    BranchList=neighbour_in_branch(BranchList=BranchList,EdgesArray=EdgesArrayUpdated,Heart=Heart)
    return BranchList
