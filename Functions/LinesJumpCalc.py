import numpy as np
def LinesJumpCalc(ZeroDraft):
    SpaceVec=np.array(ZeroDraft['Position'])
    UpSpace=SpaceVec[:-1]
    DownSpace=SpaceVec[1:]
    SpaceLines=DownSpace-UpSpace
    minSpace=np.min(SpaceLines)
    SpaceLinesNorm=np.insert(SpaceLines/minSpace,0,0)
    SpaceLinesNorm=np.array(SpaceLinesNorm,dtype=int)-1
    return SpaceLinesNorm
