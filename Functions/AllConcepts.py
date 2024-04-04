from KeyConcepts import *
from WriteSummary import *
import numpy as np
def AllConcepts(TextLines,textName,startKey="[[",endKey="]]"):    
    ConceptsList=[]
    ConceptsDB=[]
    for linecount in np.arange(len(TextLines)):   
        line=TextLines[linecount]
        ConceptsInfo=KeyConcepts(line,ConceptsDB,startKey="[[",endKey="]]")
        ConceptLine=ConceptsInfo[0]
        ConceptsDB=ConceptsInfo[1]
        Concepts=ConceptLine[0]                
        if len(Concepts)>0:
            UpdatedLine='- '+ConceptLine[1]
            TextLines[linecount]=UpdatedLine
            ConceptsList.append([Concepts,UpdatedLine,linecount])
        linecount=+1        
    ConceptsDB=list(set(ConceptsDB))
    ConceptPack=[ConceptsDB,ConceptsList,len(TextLines),TextLines] 
    WriteSummary(textName,TextLines)
    return ConceptPack
