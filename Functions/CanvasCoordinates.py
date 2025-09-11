import numpy as np
from BranchCoordinates import *
def CanvasCoordinates(Branches_and_Heart,
                      psi=0.3,
                      card_width=500,
                      card_height=120, 
                      padding=120):
    Branches=Branches_and_Heart[0]
    Heart=Branches_and_Heart[1]
    Nbranches=len(Branches)
    algleConverter=float(2*np.pi/Nbranches)
    DictCanvasCoordinates={Heart: np.zeros(2)}
    for branch in np.arange(Nbranches,dtype='int'):
        alfa=branch*algleConverter+psi
        Branch=Branches[branch][::-1]
        DictCanvasCoordinates=BranchCoordinates(alfa=alfa,
                                                Branch=Branch[1:],
                                                DictCanvasCoordinates=DictCanvasCoordinates,
                                                card_width=card_width, 
                                                card_height=card_height,
                                                padding=padding)
    return DictCanvasCoordinates
