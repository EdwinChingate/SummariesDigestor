from ConceptsExtractor import *
from Replace import *
from SaveNets import *
import os
import pandas as pd
def PoolofKnowledge_to_VOSviewerNet(mapName='Map',netName='Net'):
    Parameters=pd.read_csv('Parameters.csv',index_col=0)
    PoolofKnowledgeRute=Parameters['Value']['PoolofKnowledgeFolder']    
    startKey=Parameters['Value']['startKey']
    endKey=Parameters['Value']['endKey']
    Concepts_in_Pool=os.listdir(PoolofKnowledgeRute)
    Links=[]
    for conceptFile in Concepts_in_Pool:
        concept=Replace(conceptFile)
        textName=PoolofKnowledgeRute+'/'+conceptFile
        ConceptPack=ConceptsExtractor(textName,startKey,endKey,Write=False)
        ConceptDB=ConceptPack[0]
        ConceptDB.remove(concept)
        for conceptLinked in ConceptDB:
            Link=[concept]
            Link.append(conceptLinked)
            Link.sort()
            Links.append(Link)
    SaveNets(Concepts_in_Pool,mapName,Links,netName)
