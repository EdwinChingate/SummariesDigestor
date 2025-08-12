import json
import networkx as nx
from pathlib import Path
import numpy as np
from scores_metric import *

def create_initial_canvas(G,
                          QuestionsConceptsDF, 
                          MetricV=["degree"], 
                          N=20, 
                          canvas_path="initial.canvas",
                          card_width=420, 
                          card_height=90,
                          spacing=80):
    canvas_nodes=scores_metric(G=G, MetricV=MetricV, N=N)
    spacing_x = card_width+spacing
    spacing_y = card_height+spacing
    nodes_json = []
    row=0
    for node in canvas_nodes:
        rng = np.random.default_rng()
        random_float = rng.random()
        x = spacing_x+card_width*random_float
        y = row * spacing_y        
        text = str(QuestionsConceptsDF.iloc[node].name)
        nodes_json.append({
            "type": "text",
            "id": str(node),
            "text": text,
            "x": x,
            "y": y,
            "width": card_width,
            "height": card_height
        })
        row+=1

    # --- 4. Empty edges initially ---
    data = {
        "nodes": nodes_json,
        "edges": []
    }

    # --- 5. Save canvas ---
    Path(canvas_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    #print(f"[ok] Canvas with top {N} '{metric}' nodes saved to {canvas_path}")

