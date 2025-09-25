from AddEdge import *
def UpdateEdge(node_attractor,neighbors_attracted,CanvasDict,nodes_df):   
    card_width,card_height=nodes_df.loc[node_attractor][["width","height"]] #Here I'm using just the dimensions of the target node, as I'm assuming the size of the cards wouldn't change
    for node_near in neighbors_attracted:
        CanvasDict=AddEdge(source_node=node_near, 
                           target_node=node_attractor,
                           CanvasDict=CanvasDict,
                           card_width=card_width,
                           card_height=card_height)
    return CanvasDict

