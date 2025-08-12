from EuclideanDistance import *
import numpy as np
def CraftEuclideanDistanceMatrix(VectorsMatrix):
    NRows=VectorsMatrix.shape[0]
    EuclideanDistanceMatrix=np.zeros((NRows,NRows))
    for row_id1 in np.arange(NRows):
        V1=VectorsMatrix[row_id1,:]
        for row_id2 in np.arange(row_id1+1,NRows):
            V2=VectorsMatrix[row_id2,:]
            Distance=EuclideanDistance(V1=V1,V2=V2)
            EuclideanDistanceMatrix[row_id1,row_id2]=Distance
    return EuclideanDistanceMatrix
