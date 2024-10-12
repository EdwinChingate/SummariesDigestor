import numpy as np
import pandas as pd
def ConceptsAdjacencyMat(TextDF,ConceptsList):    
    NConcepts=len(ConceptsList)
    ConceptsMat=np.zeros((NConcepts,NConcepts))
    ConceptsDF=pd.DataFrame(ConceptsMat,index=ConceptsList,columns=ConceptsList)
    for concept in TextDF.index:
        LinesLoc=TextDF.loc[concept]==1
        Lines=TextDF.loc[concept][LinesLoc].index
        TextDF.loc[concept]=0
        for line in Lines:
            ConceptsLoc=TextDF[line]==1
            Concepts=TextDF[ConceptsLoc].index
            ConceptsDF.loc[concept][Concepts]=ConceptsDF.loc[concept][Concepts]+1
    return ConceptsDF
