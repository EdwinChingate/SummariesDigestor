import os
import pandas as pd
import numpy as np
from ReadSummary import *
def UpdateSummary():
    Parameters=pd.read_csv('Parameters.csv',index_col=0)
    TextFolder=Parameters['Value']['TextFolder']
    TextName=Parameters['Value']['TextName']    
    PoolofKnowledgeRute=Parameters['Value']['PoolofKnowledgeFolder']    
    startKey=Parameters['Value']['startKey']
    endKey=Parameters['Value']['endKey']
    if os.path.exists(PoolofKnowledgeRute)==False:
        os.mkdir(PoolofKnowledgeRute)
    textName=TextFolder+'/'+TextName
    TextDF=pd.read_excel('TextMatrix.xlsx',index_col=0)
    ConceptsDB=list(TextDF.index.copy())
    TextLines=ReadSummary(textName)
    ConceptsDF=pd.read_excel('EvaluateConcepts.xlsx',index_col=0)    
    ConceptstoUpdateLoc=ConceptsDF['Update']!=0
    if len(ConceptstoUpdateLoc)==0:
        return TextLines
    ConceptstoUpdate=ConceptsDF[ConceptstoUpdateLoc]
    ConceptstoErase=[]
    for concept in ConceptstoUpdate.index:        
        LinesVector=np.array(TextDF.loc[concept])
        LineswithconceptLoc=np.where(LinesVector==1)[0]
        newconcept=ConceptstoUpdate.loc[concept,'Update']
        try:
            conceptLocation_inDB=ConceptsDB.index(newconcept)
        except ValueError:
            conceptLocation_inDB=-1
        if conceptLocation_inDB > -1:
            TextDF.loc[newconcept]=TextDF.loc[newconcept].copy()+TextDF.loc[concept].copy()
            ConceptstoErase.append(concept)
        else:
            conceptLocation_inDB=ConceptsDB.index(concept)
            ConceptsDB[conceptLocation_inDB]=newconcept
        for linecount in LineswithconceptLoc:    
            line=TextLines[int(linecount)]
            line=line.replace(concept,newconcept)
            TextLines[int(linecount)]=line
    for concept in ConceptstoErase:
        TextDF=TextDF.drop(concept)
        ConceptsDB.remove(concept)        
    TextDF.index=ConceptsDB
    TextDF=TextDF.sort_index()    
    TextDF.to_excel('TextMatrix.xlsx')    
    return TextLines
