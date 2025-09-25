def UpdateFrames(ActiveFrameDefault,untagLeaves,nframes_df,CanvasDict,ColorsDF): 
    if not ActiveFrameDefault:
        return CanvasDict
    NodesList=CanvasDict["nodes"]
    for node in untagLeaves:
        node_id=nframes_df['position in canvas dictionary'][node]
        color=NodesList[node_id]['color']
        NodesList[node_id]['color']=ColorsDF['Complement'][color]
    CanvasDict["nodes"]=NodesList
    return CanvasDict
