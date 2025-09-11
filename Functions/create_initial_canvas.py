import json
import networkx as nx
from pathlib import Path
from scores_metric import *
from steiner_subtree_on_tree import *
from CanvasCoordinates import *
from orient_layout_by_diameter import *
from layout_to_canvas_coords import *
from build_edges_undirected_perp import *
from branches_from_the_heart import *

def create_initial_canvas(G,
                          QuestionsConceptsDF, 
                          MetricV=["degree"], 
                          N=20, 
                          canvas_path="initial.canvas",
                          psi=0.3, 
                          card_width=500, 
                          card_height=120, 
                          padding=50):
    canvas_nodes=scores_metric(G=G, 
                               MetricV=MetricV,
                               N=N)
    canvas_nodes_tree=steiner_subtree_on_tree(G=G,
                                              terminals=canvas_nodes)
    spacing_x = card_width+padding
    spacing_y = card_height+padding
    nodes_json = []
    edges_json = []
    LittleTree = G.subgraph(canvas_nodes_tree.nodes)  # induced subgraph
    Branches_and_Heart=branches_from_the_heart(LittleTree)
    #return H
    # H = ... (your Steiner or induced subgraph)
    nodes_to_render = list(LittleTree.nodes())
    
    # compute layout & convert to canvas coords
    #pos0 = compute_layout(H, layout="kamada_kawai", seed=42)  # or 'kamada_kawai'
    
    pos0=CanvasCoordinates(Branches_and_Heart=Branches_and_Heart,
                           psi=psi,
                           card_width=card_width,
                           card_height=card_height, 
                           padding=padding)
    pos1 = pos0#orient_layout_by_diameter(H, pos0, point_up=True)
    #return 0
    #return pos0
    #canvas_xy = layout_to_canvas_coords(
    #    pos1,
    #    card_width=card_width,
    #    card_height=card_height,
    #    padding=padding
    #)
    canvas_xy=pos0
    nodes_json = []    
    for node in nodes_to_render:
        text = str(QuestionsConceptsDF.iloc[int(node)].name) if str(node).isdigit() else str(node)
        x, y         = canvas_xy[node]
        #print(x, y )
        if node in list(canvas_nodes):
            color='5'
        else:
            color='6'
        nodes_json.append({
            "type": "text",
            "id": str(node),
            "text": text+' ('+str(node)+')',
            "x": int(x),
            "y": int(y),
            "width": card_width,
            "height": card_height,
            "color": color
        })

    edges_json =build_edges_undirected_perp(LittleTree, nodes_json, card_w=card_width, card_h=card_height)

    data = {"nodes": nodes_json, "edges": edges_json}

    Path(canvas_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

