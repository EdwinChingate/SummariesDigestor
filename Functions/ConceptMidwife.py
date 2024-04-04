from Phaenarete import *
from ReadSummary import *
import pandas as pd
from WriteLine import *
import numpy as np
def ConceptMidwife(textName,TextName,PoolofKnowledgeRute):
    TextDF=pd.read_excel('TextMatrix.xlsx',index_col=0)
    TextLines=ReadSummary(textName)    
    CleanName=TextName.replace('.md','')
    for concept in TextDF.index:
        Title='## '+CleanName+'\n'
        conceptFileName=PoolofKnowledgeRute+'/'+concept+'.md'
        WriteLine(line=Title,textName=conceptFileName)
        LinesVector=np.array(TextDF.loc[concept])
        LineswithconceptLoc=np.where(LinesVector==1)[0]
        Phaenarete(concept,TextLines,LineswithconceptLoc,conceptFileName)  
