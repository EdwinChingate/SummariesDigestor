import json
import networkx as nx
from pathlib import Path

def create_initial_canvas(G,
                          QuestionsConceptsDF, 
                          MetricV=["degree"], 
                          N=20, 
                          canvas_path="initial.canvas",
                          card_width=420, 
                          card_height=90,
                          spacing=80):
    canvas_nodes=scores_metric(G=G, MetricV=MetricV, N=N)
    print(canvas_nodes)
    canvas_nodes_tree=steiner_subtree_on_tree(G=G, terminals=canvas_nodes)
    print(canvas_nodes_tree.nodes)
    spacing_x = card_width+spacing
    spacing_y = card_height+spacing
    nodes_json = []
    row=0
    for node in canvas_nodes_tree.nodes:
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
    
    edges_json = []
    H = G.subgraph(canvas_nodes_tree.nodes)  # induced subgraph
    for u, v, data in H.edges(data=True):
        edges_json.append({
            "type": "edge",
            "fromNode": str(u),
            "toNode": str(v)
        })
    
    data = {
        "nodes": nodes_json,
        "edges": edges_json
    }

    nx.draw(H, with_labels=True)
    plt.show()
    nx.draw(canvas_nodes_tree, with_labels=True)
    plt.show()
    # --- 5. Save canvas ---
    #Path(canvas_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    #print(f"[ok] Canvas with top {N} '{metric}' nodes saved to {canvas_path}")

