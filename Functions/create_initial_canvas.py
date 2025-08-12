import json
import networkx as nx
from pathlib import Path

def create_initial_canvas(G, metric="degree", N=20, canvas_path="initial.canvas",
                          card_width=420, card_height=180):
    # --- 1. Compute metric ---
    if metric == "degree":
        scores = dict(G.degree())
    elif metric == "pagerank":
        scores = nx.pagerank(G)
    elif metric == "betweenness":
        scores = nx.betweenness_centrality(G)
    else:
        raise ValueError(f"Unknown metric: {metric}")

    # --- 2. Select top N nodes ---
    top_nodes = sorted(scores, key=scores.get, reverse=True)[:N]

    # --- 3. Prepare layout (grid) ---
    cols = int(N**0.5)
    spacing_x = card_width + 40
    spacing_y = card_height + 40
    nodes_json = []
    for idx, node in enumerate(top_nodes):
        row, col = divmod(idx, cols)
        x = col * spacing_x
        y = row * spacing_y
        text = G.nodes[node].get("text", str(node))
        nodes_json.append({
            "type": "text",
            "id": str(node),
            "text": text,
            "x": x,
            "y": y,
            "width": card_width,
            "height": card_height
        })

    # --- 4. Empty edges initially ---
    data = {
        "nodes": nodes_json,
        "edges": []
    }

    # --- 5. Save canvas ---
    Path(canvas_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[ok] Canvas with top {N} '{metric}' nodes saved to {canvas_path}")

