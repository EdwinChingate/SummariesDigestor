import uuid

def diagonal_anchor_pair(ax, ay, bx, by):
    """
    Compute (fromSide,toSide) for u->v and v->u so the two edges are diagonally opposed.
    Returns: (u_to_v_from, u_to_v_to, v_to_u_from, v_to_u_to)
    """
    dx, dy = bx - ax, by - ay
    # vertical choice based on who is visually above/below
    if abs(dy) >= abs(dx):
        # v is mostly above/below u
        u_from = "bottom" if dy > 0 else "top"
        v_from = "top" if dy > 0 else "bottom"
        # horizontal sides to keep diagonal
        # if v is to the right of u, land on v's left; else on v's right
        u_to   = "left" if dx > 0 else "right"
        # and the opposite for the reverse edge landing on u
        v_to   = "right" if dx > 0 else "left"
    else:
        # mostly horizontal separation; make a symmetric diagonal choice
        u_from = "right" if dx > 0 else "left"
        v_from = "left"  if dx > 0 else "right"
        u_to   = "top"   if dy < 0 else "bottom"
        v_to   = "bottom" if dy < 0 else "top"
    return u_from, u_to, v_from, v_to
