from KeyConcept import *
def KeyConcepts(line,ConceptsDB,startKey="[[",endKey="]]"):
    concept='letsgo'
    UpdatedLine=line
    line=line+concept
    Concepts=[]
    while True:
        conceptDataInf=KeyConcept(line,UpdatedLine,ConceptsDB,startKey,endKey)
        if conceptDataInf==0:
            break        
        conceptData=conceptDataInf[0]
        ConceptsDB=conceptDataInf[1]
        concept=conceptData[0]
        newstart=conceptData[1]+2
        UpdatedLine=conceptData[2]
        line=line[newstart:]
        Concepts.append(concept)
    ConceptLine=[Concepts,UpdatedLine]
    ConceptsInfo=[ConceptLine,ConceptsDB]
    return ConceptsInfo
