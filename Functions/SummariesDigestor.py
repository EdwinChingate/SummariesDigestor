from ConceptsExtractor import *
from Replace import *
import os
def SummariesDigestor():
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
    ConceptsinPool=os.listdir(PoolofKnowledgeRute)
    conceptsPool=list(map(Replace,ConceptsinPool))
    FutureConceptsPool=set(conceptsPool+ConceptsDB)
    TotalConceptsNumber=len(FutureConceptsPool)
    conceptsPoolDF=pd.DataFrame(FutureConceptsPool,index=FutureConceptsPool,columns=['Concept'])
    conceptsPoolDF['Pool']=0
    conceptsPoolDF['Summary']=0
    conceptsPoolDF.loc[ConceptsDB,'Summary']=1
    conceptsPoolDF.loc[conceptsPool,'Pool']=1
    conceptsPoolDF['New']=(1-conceptsPoolDF['Pool']*conceptsPoolDF['Summary'])*conceptsPoolDF['Summary']
    conceptsPoolDF['Update']=0
    conceptsPoolDF=conceptsPoolDF.sort_index()
    conceptsPoolDF.to_excel('EvaluateConcepts.xlsx')
