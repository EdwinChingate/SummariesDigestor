import numpy as np
#from neighbour_in_branch import *
def branches_from_the_heart(TreeSeed):
    DegreeArray=np.array(TreeSeed.degree,dtype='int')
    LeavesLoc=np.where(DegreeArray[:,1]==1)[0]
    LeavesList=DegreeArray[LeavesLoc,0]
    top_nodes=np.array(sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:5])
    # I can also strength the function to consider several candidates to heart
    #Top_betweenness_centrality=np.array([betweenness_centrality[key] for key in top_nodes])
    #Top_betweenness_centrality=Max_betweenness_centrality
    #Max_betweenness_centrality=max(Top_betweenness_centrality)
    #HeartLoc=np.where(Top_betweenness_centrality==Max_betweenness_centrality)[0]
    #Heart=top_nodes[int(Max_betweenness_centrality_loc[0])]
    Heart=top_nodes[0]    
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
