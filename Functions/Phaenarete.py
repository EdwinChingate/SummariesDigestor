def Phaenarete(ConceptLine,PoolofKnowledgeRute):
    Concepts=ConceptLine[0]
    line=ConceptLine[1]
    for concept in Concepts:
        conceptFileName=PoolofKnowledgeRute+'/'+concept+'.md'
        with open(conceptFileName,'a') as ConceptFile:
            ConceptFile.write(line)   
