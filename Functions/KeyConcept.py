def KeyConcept(line,startKey="[[",endKey="]]"):
    start=line.find(startKey)+2
    end=line.find(endKey)
    concept=line[start:end]
    concept=concept.replace(' ','_')
    if start==1 or concept[-4:]=='.png':
        return 0
    return([concept,end])
