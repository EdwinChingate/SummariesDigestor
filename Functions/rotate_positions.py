import numpy as np
import math

def rotate_positions(pos, angle_rad, center=None):
    """Rotate positions dict by angle (in radians) around center (x0,y0)."""
    if center is None:
        xs = np.array([p[0] for p in pos.values()], float)
        ys = np.array([p[1] for p in pos.values()], float)
        center = (float(xs.mean()), float(ys.mean()))
    cx, cy = center
    c, s = math.cos(angle_rad), math.sin(angle_rad)
    out = {}
    for n, (x, y) in pos.items():
        X, Y = x - cx, y - cy
        xr = c*X - s*Y
        yr = s*X + c*Y
        out[n] = (xr + cx, yr + cy)
    return out
