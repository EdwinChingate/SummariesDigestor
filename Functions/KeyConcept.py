def KeyConcept(line,UpdatedLine,ConceptsDB,startKey="[[",endKey="]]"):
    start=line.find(startKey)+2
    end=line.find(endKey)
    concept=line[start:end]
    oldconcept=concept
    concept=concept.replace(' ','_')
    UpdatedLine=UpdatedLine.replace(oldconcept,concept)
    if start==1 or concept[-4:]=='.png':
        return 0
    ConceptsDB.append(concept)
    conceptData=[concept,end,UpdatedLine]
    conceptDataInf=[conceptData,ConceptsDB]
    return conceptDataInf
