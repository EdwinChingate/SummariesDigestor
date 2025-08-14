import math
from longest_path_in_tree import *
from rotate_positions import *

def orient_layout_by_diameter(G, pos, point_up=True):
    """
    Rotate layout so the diameter path is vertical.
    If point_up=True, u->v points up (positive y before Canvas flip).
    """
    u,v,_=longest_path_in_tree(G)
    (x1, y1), (x2, y2) = pos[u], pos[v]
    dx, dy = (x2 - x1), (y2 - y1)
    angle_now = math.atan2(dy, dx)        # current angle of diameter
    angle_target = math.pi/2 if point_up else -math.pi/2  # vertical
    theta = angle_target - angle_now
    return rotate_positions(pos, theta)
