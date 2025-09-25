def UpdateCanvasDict(CanvasDict,LeavesSet,nodes_df,not_branching_cards):
    NodesList=CanvasDict["nodes"]
    nodes_df.loc[not_branching_cards,'branches']=0    
    for node in LeavesSet:
        node_id=nodes_df["position in canvas dictionary"][node]
        default_color=NodesList[node_id]["default_color"]        
        NodesList[node_id]['color']=default_color
        NodesList[node_id]['branches']=int(nodes_df['branches'][node])
    CanvasDict["nodes"]=NodesList    
    return CanvasDict
