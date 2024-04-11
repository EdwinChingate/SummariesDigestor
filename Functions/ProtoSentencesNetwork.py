from SaveNets import *
import pandas as pd
from LinkSentences import *
def ProtoSentencesNetwork(mapName='ProtoSentenceMap',netName='ProtoSentenceNet'):
    Parameters=pd.read_csv('Parameters.csv',index_col=0)
    KnowledgeNetworksRute=Parameters['Value']['KnowledgeNetworksFolder']
    NetworkName=Parameters['Value']['NetworkName']
    networkName=KnowledgeNetworksRute+'/'+NetworkName
    Network=pd.read_csv(networkName)
    Network['ProtoSentence']=Network['source']+'|'+Network['target']
    ConceptsDB=list(set(list(Network['source'])+list(Network['target'])))
    Links=[]
    for concept in ConceptsDB[:10]:
        SentencesLoc=(Network['source']==concept)|(Network['target']==concept)
        links=list(Network[SentencesLoc]['ProtoSentence'])
        Links=LinkSentences(Links,links)
    SaveNets(Concepts_in_Pool=Network['ProtoSentence'],mapName=mapName,Links=Links,netName=netName)    
