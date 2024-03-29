from KeyConcepts import *
def AllConcepts(TextLines,startKey="[[",endKey="]]"):    
    ConceptsList=[]
    ConceptsDB=[]
    for line in TextLines:        
        ConceptsInfo=KeyConcepts(line,ConceptsDB,startKey="[[",endKey="]]")
        ConceptLine=ConceptsInfo[0]
        ConceptsDB=ConceptsInfo[1]
        Concepts=ConceptLine[0]
        UpdatedLine='- '+ConceptLine[1]
        if len(Concepts)>0:
            ConceptsList.append([Concepts,UpdatedLine])
    ConceptsDB=set(ConceptsDB)
    print(ConceptsDB)
    return ConceptsList
