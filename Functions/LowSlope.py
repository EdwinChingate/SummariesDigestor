import numpy as np
def LowSlope(Branch,
             slope,
             upside_direction,
             DictCanvasCoordinates,
             card_width=500, 
             padding=200,
             Distance_from_heart=3):
    Ncards=len(Branch)  
    slope_sign=np.sign(slope)
    rightside_direction=upside_direction*slope_sign
    for card in np.arange(Ncards,dtype='int'):
        node=Branch[card]
        x=rightside_direction*(int(card)+Distance_from_heart)*(card_width+padding)
        y=x*slope
        DictCanvasCoordinates[node]=np.array([int(x),int(y)])    
    return DictCanvasCoordinates
        
