from ConceptsExtractor import *
from Replace import *
import os
import pandas as pd
def PoolofKnowledge_to_CytoscapeNet(fileName='Network'):
    Parameters=pd.read_csv('Parameters.csv',index_col=0)
    PoolofKnowledgeRute=Parameters['Value']['PoolofKnowledgeFolder']    
    startKey=Parameters['Value']['startKey']
    endKey=Parameters['Value']['endKey']
    FileName=fileName+'.csv'
    network=open(FileName,'w')
    network.write('source,target\n')
    network.close()
    ConceptsinPool=os.listdir(PoolofKnowledgeRute)
    for conceptFile in ConceptsinPool:
        concept=Replace(conceptFile)
        textName=PoolofKnowledgeRute+'/'+conceptFile
        ConceptPack=ConceptsExtractor(textName,startKey,endKey,Write=False)
        ConceptDB=ConceptPack[0]
        ConceptDB.remove(concept)
        print(concept)
        #Add something to remove duplicates
        for x in ConceptDB:
            with open(FileName,'a') as network:
                network.write(concept+','+x+'\n')
            network.close()
