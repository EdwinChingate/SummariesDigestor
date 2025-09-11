import numpy as np
def HighSlope(Branch,
              slope,
              upside_direction,
              DictCanvasCoordinates,
              card_height=120, 
              padding=200,
              Distance_from_heart=3):
    Ncards=len(Branch)    
    for card in np.arange(Ncards,dtype='int'):
        node=Branch[card]
        y=upside_direction*(int(card)+Distance_from_heart)*(card_height+padding)
        x=y/slope
        DictCanvasCoordinates[node]=np.array([int(x),int(y)])    
    return DictCanvasCoordinates        
