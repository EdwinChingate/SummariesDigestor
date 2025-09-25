import numpy as np
def DeleteEmptyFrames(goneNodes,CanvasDict,nframes_df):
    if len(goneNodes)==0:        
        return CanvasDict
    NodesList=CanvasDict["nodes"]
    CleanNodesList=[]
    N_cards_in_canvas=len(NodesList)
    Cards_id_set=set(np.arange(N_cards_in_canvas).tolist())
    goneNodes_cavas_id=set(nframes_df['position in canvas dictionary'][list(goneNodes)])
    active_cards=Cards_id_set-goneNodes_cavas_id
    for card in active_cards:
        CleanNodesList.append(NodesList[card])
    CanvasDict["nodes"]=CleanNodesList
    return CanvasDict
