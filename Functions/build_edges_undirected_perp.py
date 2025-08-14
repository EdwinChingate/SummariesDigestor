import uuid
from closest_side_pair import *

def build_edges_undirected_perp(G, nodes_json, card_w=420, card_h=120):
    pos = {n["id"]: (n["x"], n["y"]) for n in nodes_json}
    edges = []
    for u, v in G.edges():
        uid, vid = str(u), str(v)
        if uid not in pos or vid not in pos:
            continue
        (ux, uy), (vx, vy) = pos[uid], pos[vid]
        u_from, v_to = closest_side_pair(ux, uy, vx, vy, card_w, card_h)
        edges.append({
            "id": uuid.uuid4().hex,
            "fromNode": uid, "fromSide": u_from,
            "toNode":   vid, "toSide":   v_to,
            "toEnd":"none"
        })
    return edges
