import uuid

def choose_sides(ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    # prefer vertical anchoring when |dy| >= |dx|
    if abs(dy) >= abs(dx):
        from_side = "bottom" if dy > 0 else "top"
        to_side   = "top"    if dy > 0 else "bottom"
    else:
        from_side = "right"  if dx > 0 else "left"
        to_side   = "left"   if dx > 0 else "right"
    return from_side, to_side
