import numpy as np

def norm(a):
    a_min, a_max = float(a.min()), float(a.max())
    if a_max - a_min < 1e-12:
        return np.zeros_like(a)  # degenerate case
    return (a - a_min) / (a_max - a_min)
