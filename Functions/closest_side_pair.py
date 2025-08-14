def closest_side_pair(ax, ay, bx, by, card_w=420, card_h=120):
    """
    Pick anchors for a single undirected edge from u(ax,ay) -> v(bx,by)
    using rectangle extents. We compute the separations between the 1D
    projections along X and Y, then CONNECT ALONG THE PERPENDICULAR AXIS
    to the smallest separation, as requested.

    Returns: (fromSide_u, toSide_v)
    """
    # Rect extents (top-left origin)
    ax0, ax1 = ax, ax + card_w
    ay0, ay1 = ay, ay + card_h
    bx0, bx1 = bx, bx + card_w
    by0, by1 = by, by + card_h

    # 1D interval separation (0 if overlapping)
    def sep_1d(a0, a1, b0, b1):
        if a1 < b0:  # a is left/above b
            return b0 - a1
        if b1 < a0:  # b is left/above a
            return a0 - b1
        return 0.0  # overlap

    sep_x = sep_1d(ax0, ax1, bx0, bx1)
    sep_y = sep_1d(ay0, ay1, by0, by1)

    # centers for orientation
    ucx, ucy = ax0 + card_w/2, ay0 + card_h/2
    vcx, vcy = bx0 + card_w/2, by0 + card_h/2
    dx, dy = vcx - ucx, vcy - ucy

    # Choose connection axis = perpendicular to the smallest separation axis
    # - if sep_x is smallest, connect VERTICALLY (bottom/top)
    # - if sep_y is smallest, connect HORIZONTALLY (right/left)
    if sep_x <= sep_y:
        # vertical connection
        from_side = "bottom" if dy > 0 else "top"
        to_side   = "top"    if dy > 0 else "bottom"
    else:
        # horizontal connection
        from_side = "right" if dx > 0 else "left"
        to_side   = "left"  if dx > 0 else "right"

    return from_side, to_side

