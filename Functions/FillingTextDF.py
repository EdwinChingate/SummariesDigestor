import pandas as pd
import numpy as np
def FillingTextDF(ConceptsDB,ConceptsList,linesNumber):
    ConceptsNumber=len(ConceptsDB)
    TextMatrix=np.zeros([ConceptsNumber,linesNumber])    
    TextDF=pd.DataFrame(TextMatrix,index=ConceptsDB,columns=np.arange(linesNumber))
    for ConceptLine in ConceptsList:  
        Concepts=ConceptLine[0]
        LinePosition=ConceptLine[2]        
        TextDF.loc[Concepts,LinePosition]=1        
    return TextDF
