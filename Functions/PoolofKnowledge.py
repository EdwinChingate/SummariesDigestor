import numpy as np
import os
import pandas as pd
from ConceptsExtractor import *
from ReferenceMidwife import *
from ConceptMidwife import *
def PoolofKnowledge():
    Parameters=pd.read_csv('Parameters.csv',index_col=0)
    TextFolder=Parameters['Value']['TextFolder']
    TextName=Parameters['Value']['TextName']    
    PoolofKnowledgeRute=Parameters['Value']['PoolofKnowledgeFolder']    
    startKey=Parameters['Value']['startKey']
    endKey=Parameters['Value']['endKey']
    if os.path.exists(PoolofKnowledgeRute)==False:
        os.mkdir(PoolofKnowledgeRute)
    textName=TextFolder+'/'+TextName
    ConceptPack=ConceptsExtractor(textName,startKey,endKey)
    ConceptsList=ConceptPack[1]
    ConceptsDB=ConceptPack[0]    
    ReferenceMidwife(ConceptsDB,TextName,PoolofKnowledgeRute)
    ConceptMidwife(ConceptsList,PoolofKnowledgeRute)    
