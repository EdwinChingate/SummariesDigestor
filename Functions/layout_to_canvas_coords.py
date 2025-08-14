import numpy as np
from norm import *

def layout_to_canvas_coords(pos, card_width=420, card_height=120, padding=120):
    """
    Map layout coords -> Obsidian Canvas pixel coords.
    - Normalizes x,y to a positive pixel range.
    - Flips y (NetworkX y up, Canvas y down).
    Returns dict {node: (X_px, Y_px)} with top-left corner for the card.
    """
    xs = np.array([p[0] for p in pos.values()], dtype=float)
    ys = np.array([p[1] for p in pos.values()], dtype=float)
    # normalize to [0,1]
    xn = norm(xs)
    yn = norm(ys)
    # flip y for Canvas (down is positive)
    yn = 1.0 - yn
    # choose a canvas envelope; leave padding around cards
    # spacing scaled so cards don't overlap by default
    X_span = (card_width  + 4*padding) * max(1, int(np.ceil(len(pos)**0.5)))
    Y_span = (card_height + 4*padding) * max(1, int(np.ceil(len(pos)**0.5)))
    X0, Y0 = padding, padding
    X = X0 + xn * (X_span - card_width  - 2*padding)
    Y = Y0 + yn * (Y_span - card_height - 2*padding)
    return {n: (int(x), int(y)) for n, x, y in zip(pos.keys(), X, Y)}
