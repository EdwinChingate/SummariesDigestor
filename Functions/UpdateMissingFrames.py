def UpdateMissingFrames(tagLeaves,CanvasDict,nodes_df,ColorsDF,ActiveFrameDefault,
                        padding=70):
    #I guess I can also get the padding back from the cards distribution itself
    NodesList=CanvasDict["nodes"]
    nodes_json=[]
    for node in tagLeaves:         
        x,y,card_width,card_height,color=nodes_df.loc[node][["x","y","width","height","default_color"]]
        ColorList=[ColorsDF['Complement'][color],color]
        nodes_json.append({
                    "type": "group",
                    "id": str(node)+'G',
                    "x": int(x)-padding*0.3,
                    "y": int(y)-padding*0.3,            
                    "width": int(card_width)+padding*0.6,
                    "height": int(card_height)+padding*0.6,
                    "color": ColorList[int(ActiveFrameDefault)]
                })
    NodesList=NodesList+nodes_json
    CanvasDict["nodes"]=NodesList
    return CanvasDict        
