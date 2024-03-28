from KeyConcept import *
def KeyConcepts(line,startKey="[[",endKey="]]"):
    concept='letsgo'
    line=line+concept
    Concepts=[]
    while True:
        conceptData=KeyConcept(line,startKey,endKey)
        if conceptData==0:
            break
        concept=conceptData[0]
        newstart=conceptData[1]+2
        line=line[newstart:]
        Concepts.append(concept)
    return Concepts
