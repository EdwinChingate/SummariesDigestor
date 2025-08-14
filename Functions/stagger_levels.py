import numpy as np
from level_by_distance import *

def stagger_levels(pos, G, root, base_shift=300):
    """
    Zig-zag x for each level so connected nodes are not aligned.
    base_shift ~ pixels before final canvas scaling (pre-normalization units).
    """
    level = level_by_distance(G, root)
    # group nodes by level
    lev2nodes = {}
    for n, lv in level.items():
        lev2nodes.setdefault(lv, []).append(n)

    pos2 = dict(pos)
    for lv, nodes in lev2nodes.items():
        # alternate left/right per level and also spread inside the level
        # e.g., [-1, +1, -1.5, +1.5, ...] * base_shift
        offsets = []
        sign = -1 if lv % 2 == 0 else +1
        for i, _ in enumerate(nodes):
            # interleave offsets: 1, 1.3, 1.6, ...
            offsets.append(sign * (1.0 + 0.3 * (i // 1)))
        # center them by subtracting mean
        offsets = np.array(offsets)
        offsets = offsets - offsets.mean()
        for off, n in zip(offsets, nodes):
            x, y = pos2[n]
            pos2[n] = (x + off * base_shift, y)
    return pos2

