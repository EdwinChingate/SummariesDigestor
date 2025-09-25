import uuid
from closest_side_pair import *
def AddEdge(source_node,target_node,CanvasDict,
            card_width=500,
            card_height=120):
    NodesList=CanvasDict["nodes"]
    EdgesList=CanvasDict['edges']
    source_node_id, target_node_id = str(source_node), str(target_node)
    pos = {n["id"]: (n["x"], n["y"]) for n in NodesList}
    (source_node_x, source_node_y), (target_node_x, target_node_y) = pos[source_node_id], pos[target_node_id]
    source_node_from, target_node_to = closest_side_pair(ax=source_node_x,
                                                         ay=source_node_y, 
                                                         bx=target_node_x, 
                                                         by=target_node_y, 
                                                         card_w=card_width, 
                                                         card_h=card_height)
    EdgesList.append({
            "id": uuid.uuid4().hex,
            "fromNode": source_node_id, "fromSide": source_node_from,
            "toNode":   target_node_id, "toSide": target_node_to,
            "toEnd":"none"
        })
    CanvasDict['edges']=EdgesList
    return CanvasDict
