import math

def anti_align_connected(canvas_xy, G, card_w=420, card_h=120,
                         dx_min=None, dy_min=None, iters=2, prefer='leaf'):
    """
    Ensure every edge u—v has BOTH |dx|>=dx_min and |dy|>=dy_min by nudging one endpoint.
    - canvas_xy: dict {node: (x_px, y_px)} TOP-LEFT corners
    - prefer: 'leaf' nudges leaves more often; 'lowdeg' nudges lower-degree endpoint
    """
    if dx_min is None: dx_min = int(card_w * 0.35)   # ~1/3 card width
    if dy_min is None: dy_min = int(card_h * 0.35)   # ~1/3 card height

    # Work with centers; easier to reason about diagonals
    ctr = {n: (x + card_w//2, y + card_h//2) for n,(x,y) in canvas_xy.items()}

    def pick_endpoint(u, v):
        if prefer == 'leaf':
            du, dv = G.degree(u), G.degree(v)
            # nudge the one with smaller degree (likely a leaf)
            return u if du < dv else v
        elif prefer == 'lowdeg':
            du, dv = G.degree(u), G.degree(v)
            return u if du <= dv else v
        # default: whichever id sorts later (simple tie-break)
        return v if str(v) > str(u) else u

    for _ in range(iters):
        moved = 0
        for u, v in G.edges():
            if u not in ctr or v not in ctr: 
                continue
            ux, uy = ctr[u]
            vx, vy = ctr[v]
            dx = vx - ux
            dy = vy - uy

            need_x = abs(dx) < dx_min
            need_y = abs(dy) < dy_min
            if not (need_x or need_y):
                continue

            # Which node to nudge?
            m = pick_endpoint(u, v)
            mx, my = ctr[m]

            # Choose directions so edges become diagonals and don't collapse back
            # Push horizontally away and vertically away
            sx = 1 if (vx >= ux) else -1
            sy = 1 if (vy >= uy) else -1
            jiggle_x = sx * (dx_min - abs(dx)) if need_x else 0
            jiggle_y = sy * (dy_min - abs(dy)) if need_y else 0

            ctr[m] = (mx + int(jiggle_x), my + int(jiggle_y))
            moved += 1

        if moved == 0:
            break

    # write centers back to top-left corners
    out = {n: (cx - card_w//2, cy - card_h//2) for n,(cx,cy) in ctr.items()}
    return out


