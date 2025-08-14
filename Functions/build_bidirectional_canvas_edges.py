import uuid  
from diagonal_anchor_pair import *

def build_bidirectional_canvas_edges(H, nodes_json):
    """Emit two Canvas edges per undirected edge (u—v) with diagonal anchors."""
    pos_lookup = {n["id"]: (n["x"], n["y"]) for n in nodes_json}
    edges_out = []
    for u, v, _ in H.edges(data=True):
        uid, vid = str(u), str(v)
        if uid not in pos_lookup or vid not in pos_lookup:
            continue
        (ux, uy), (vx, vy) = pos_lookup[uid], pos_lookup[vid]
        u_from, u_to, v_from, v_to = diagonal_anchor_pair(ux, uy, vx, vy)

        edges_out.append({
            "id": uuid.uuid4().hex,
            "fromNode": uid, "fromSide": u_from,
            "toNode":   vid, "toSide":   u_to
        })
        edges_out.append({
            "id": uuid.uuid4().hex,
            "fromNode": vid, "fromSide": v_from,
            "toNode":   uid, "toSide":   v_to
        })
    return edges_out

