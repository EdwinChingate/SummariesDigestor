def ReferenceMidwife(ConceptsDB,TextName,PoolofKnowledgeRute):
    CleanName=TextName.replace('.md','')
    Title='## '+CleanName+'\n'
    for concept in ConceptsDB:
        conceptFileName=PoolofKnowledgeRute+'/'+concept+'.md'
        with open(conceptFileName,'a') as ConceptFile:
            ConceptFile.write(Title)   
