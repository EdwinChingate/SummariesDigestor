import json
import pandas as pd
from reconstruct_network_from_canvas import *
from UpdateEdges import *
from UpdateLeaves import *
from DeleteEmptyFrames import *
def UpdateCanvas(routeCanvas,
                 MaximumSimilarityTree,
                 ActiveFrameDefault=False,
                 padding=70):
    routeLog=routeCanvas.replace('.canvas','.xlsx')
    ColorsDF=pd.read_csv('Colors.csv',index_col=0)
    WritingTree,nodes_df, edges_df,CanvasDict,nframes_df=reconstruct_network_from_canvas(path_or_dict=routeCanvas,
                                                                                         cast_ids=True, 
                                                                                         undirected=True)
    
    #StatusDF=pd.read_excel(routeLog,index_col=0) Missing updating the log file
    LeavesLoc=nodes_df['branches']>0
    LeavesSet=set(nodes_df[LeavesLoc].index)      
    nodes_ids=set(nodes_df.index)
    frames_ids=set(nframes_df.index)
    tagLeaves=LeavesSet-frames_ids
    goneNodes=frames_ids-nodes_ids        
    CanvasDict=UpdateEdges(goneNodes=goneNodes,
                           WritingTree=WritingTree,
                           MaximumSimilarityTree=MaximumSimilarityTree,
                           CanvasDict=CanvasDict,
                           nodes_df=nodes_df)    
    CanvasDict=UpdateLeaves(tagLeaves=tagLeaves,
                            LeavesSet=LeavesSet,
                            nodes_ids=nodes_ids,
                            frames_ids=frames_ids,
                            nodes_df=nodes_df,
                            nframes_df=nframes_df,
                            CanvasDict=CanvasDict,
                            ColorsDF=ColorsDF,
                            padding=padding,
                            ActiveFrameDefault=ActiveFrameDefault)
    CanvasDict=DeleteEmptyFrames(goneNodes=goneNodes,
                                 CanvasDict=CanvasDict,
                                 nframes_df=nframes_df)
    
    Path(routeCanvas).write_text(json.dumps(CanvasDict, ensure_ascii=False, indent=2), encoding="utf-8")
    #I need another function just to manipute the log file
    return CanvasDict
