import numpy as np
import os
import pandas as pd
from ConceptMidwife import *
from WriteSummary import *
from UpdateSummary import *
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
    TextLines=UpdateSummary()
    WriteSummary(textName,TextLines)
    ConceptMidwife(textName,TextName,PoolofKnowledgeRute)  
