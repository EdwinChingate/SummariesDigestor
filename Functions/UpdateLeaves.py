from UpdateCanvasDict import *
from UpdateMissingFrames import *
from UpdateFrames import *
def UpdateLeaves(tagLeaves,LeavesSet,nodes_ids,frames_ids,nodes_df,nframes_df,CanvasDict,ColorsDF,
                 padding=70,
                 ActiveFrameDefault=False):
    if len(tagLeaves)==0:
        return CanvasDict
    untagLeaves=LeavesSet-tagLeaves
    tagLeavesList=[untagLeaves,tagLeaves]
    not_branching_cards=list(tagLeavesList[int(ActiveFrameDefault)])
    CanvasDict=UpdateCanvasDict(CanvasDict=CanvasDict,
                                LeavesSet=LeavesSet,
                                nodes_df=nodes_df,
                                not_branching_cards=not_branching_cards)
    CanvasDict=UpdateMissingFrames(tagLeaves=tagLeaves,
                                   CanvasDict=CanvasDict,
                                   nodes_df=nodes_df,
                                   ColorsDF=ColorsDF,
                                   ActiveFrameDefault=ActiveFrameDefault,
                                   padding=padding)         
    CanvasDict=UpdateFrames(ActiveFrameDefault=ActiveFrameDefault,
                            untagLeaves=untagLeaves,
                            nframes_df=nframes_df,
                            CanvasDict=CanvasDict,
                            ColorsDF=ColorsDF)
    return CanvasDict
    
