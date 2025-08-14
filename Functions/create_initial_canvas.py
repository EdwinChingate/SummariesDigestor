import json
import networkx as nx
from pathlib import Path
from scores_metric import *
from steiner_subtree_on_tree import *
from compute_layout import *
from orient_layout_by_diameter import *
from layout_to_canvas_coords import *
from build_edges_undirected_perp import *

def create_initial_canvas(G,
                          QuestionsConceptsDF, 
                          MetricV=["degree"], 
                          N=20, 
                          canvas_path="initial.canvas",
                          card_width=420, 
                          card_height=90,
                          spacing=80):
    canvas_nodes=scores_metric(G=G, MetricV=MetricV, N=N)
    canvas_nodes_tree=steiner_subtree_on_tree(G=G, terminals=canvas_nodes)
    spacing_x = card_width+spacing
    spacing_y = card_height+spacing
    nodes_json = []
    edges_json = []
    H = G.subgraph(canvas_nodes_tree.nodes)  # induced subgraph
    
    # H = ... (your Steiner or induced subgraph)
    nodes_to_render = list(H.nodes())

    # compute layout & convert to canvas coords
    pos0 = compute_layout(H, layout="spring", seed=42)  # or 'kamada_kawai'
    
    pos1 = orient_layout_by_diameter(H, pos0, point_up=True)
  
    canvas_xy = layout_to_canvas_coords(
        pos1,
        card_width=card_width,
        card_height=card_height,
        padding=spacing
    )
    
    nodes_json = []    
    for node in nodes_to_render:
        text = str(QuestionsConceptsDF.iloc[int(node)].name) if str(node).isdigit() else str(node)
        x, y = canvas_xy[node]
        if node in list(canvas_nodes):
            color='5'
        else:
            color='6'
        nodes_json.append({
            "type": "text",
            "id": str(node),
            "text": text+' ('+str(node)+')',
            "x": x,
            "y": y,
            "width": card_width,
            "height": card_height,
            "color": color
        })

    edges_json =build_edges_undirected_perp(H, nodes_json, card_w=420, card_h=120)

    data = {"nodes": nodes_json, "edges": edges_json}

    Path(canvas_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

