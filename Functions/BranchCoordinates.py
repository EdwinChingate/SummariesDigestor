import numpy as np
from HighSlope import *
from LowSlope import *
def BranchCoordinates(alfa,
                      Branch,
                      DictCanvasCoordinates,
                      card_width=500, 
                      card_height=120,
                      padding=200):
    slope=np.tan(alfa)
    card_slope=card_height/card_width  
    upside_direction=np.sign(np.sin(alfa))    
    if abs(slope)>=card_slope:
        DictCanvasCoordinates=HighSlope(Branch=Branch,
                                        slope=slope,
                                        upside_direction=upside_direction,
                                        DictCanvasCoordinates=DictCanvasCoordinates,
                                        card_height=card_height, 
                                        padding=padding)
    else:
        DictCanvasCoordinates=LowSlope(Branch=Branch,
                                       slope=slope,
                                       upside_direction=upside_direction,
                                       DictCanvasCoordinates=DictCanvasCoordinates,
                                       card_width=card_width, 
                                       padding=padding)
    return DictCanvasCoordinates
