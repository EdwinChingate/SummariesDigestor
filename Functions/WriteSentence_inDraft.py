from WriteLine import *
def WriteSentence_inDraft(DraftName,TextLines,concept2,ReferenceInd='##'):
    for line in TextLines:
        ConceptLoc=line.find(concept2)
        ReferenceLoc=line.find(ReferenceInd)
        if ReferenceLoc > -1:
            Reference=line.replace(ReferenceInd,'')
        if ConceptLoc>-1:        
            WriteLine(line+Reference,DraftName)
