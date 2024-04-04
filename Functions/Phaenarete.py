def Phaenarete(concept,TextLines,LineswithconceptLoc,conceptFileName):    
    for linecount in LineswithconceptLoc:    
        line=TextLines[int(linecount)]
        with open(conceptFileName,'a') as ConceptFile:
            ConceptFile.write(line)  
