import pandas as pd
import os
from ConceptsExtractor import *
from ConceptsAdjacencyMat import *
from WriteSummaryNetwork import *
def SummaryNetwork(Home=True):
    Parameters=pd.read_csv('Parameters.csv',index_col=0)
    if Home:
        TextFolder=os.getcwd()
    else:    
        TextFolder=Parameters['Value']['TextFolder']
    TextName=Parameters['Value']['TextName']    
    PoolofKnowledgeRute=Parameters['Value']['PoolofKnowledgeFolder']    
    startKey=Parameters['Value']['startKey']
    endKey=Parameters['Value']['endKey']
    textName=TextFolder+'/'+TextName
    TextDF=ConceptsExtractor(textName,startKey="[[",endKey="]]",WriteDF=True,Write=False, ReturnConceptPack=False)
    ConceptsList=list(TextDF.index)
    ConceptsDF=ConceptsAdjacencyMat(TextDF,ConceptsList)
    WriteSummaryNetwork(ConceptsList,ConceptsDF,TextName)
