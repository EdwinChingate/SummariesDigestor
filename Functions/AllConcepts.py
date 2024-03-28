from KeyConcepts import *
def AllConcepts(TextLines,startKey="[[",endKey="]]"):    
    ConceptsList=[]
    for line in TextLines:
        Concepts=KeyConcepts(line)
        if len(Concepts)>0:
            ConceptsList.append([Concepts,line])
    return ConceptsList
