import numpy as np
import pandas as pd
from load_canvas import *
from maybe_int import *
def tables_from_canvas(canvas,
                       cast_ids=True,
                       BranchExpKey='\nBranches:',
                       card_width=500):
    CanvasDict=load_canvas(path_or_dict=canvas)
    nrows = []
    nframes=[]
    position_count=0
    NodesList=CanvasDict["nodes"]
    EdgesList=CanvasDict['edges']
    for n in NodesList:
        nid = maybe_int(n.get("id")) if cast_ids else n.get("id")
        CellType=str(n.get("type"))
        if CellType=="text":
            nrows.append({
                "id": nid, 
                "text":n.get("text"),
                "branches":n.get("branches"),
                "min layers":n.get("min"),
                "max layers":n.get("max"),
                "layer": n.get("layer"),
                "x": n.get("x"), 
                "y": n.get("y"),
                "width": n.get("width"), 
                "height": n.get("height"),
                "heart":n.get("heart"),
                "color": n.get("color"),
                "default_color":n.get("default_color"),
                "position in canvas dictionary":position_count})
        else:
            nframes.append({
               "id": int(str(nid).replace('G','')),
                "color": n.get("color"),
                "position in canvas dictionary":position_count
            })
        position_count+=1
    nodes_df=pd.DataFrame(nrows)
    indexList=list(nodes_df.index)
    nodes_df.set_index("id", inplace=True)
    nframes_df=pd.DataFrame(nframes)
    nframes_df.set_index("id", inplace=True)
    erows = []
    for e in EdgesList:
        u = maybe_int(e.get("fromNode")) if cast_ids else e.get("fromNode")
        v = maybe_int(e.get("toNode"))   if cast_ids else e.get("toNode")
        erows.append({
            "id": e.get("id"),
            "source": u, "target": v,
            "fromSide": e.get("fromSide"),
            "toSide": e.get("toSide"),
            "toEnd": e.get("toEnd")})
    edges_df = pd.DataFrame(erows)
    return nodes_df, edges_df,nframes_df
