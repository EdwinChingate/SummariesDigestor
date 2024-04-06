from AllConcepts import *
from ReadSummary import *
from FillingTextDF import *
def ConceptsExtractor(textName,startKey="[[",endKey="]]",Write=True):
    TextLines=ReadSummary(textName)
    ConceptPack=AllConcepts(TextLines,textName,startKey,endKey,Write)
    if Write:
        linesNumber=ConceptPack[2]
        ConceptsList=ConceptPack[1]
        ConceptsDB=ConceptPack[0]
        TextDF=FillingTextDF(ConceptsDB,ConceptsList,linesNumber)
        TextDF=TextDF.sort_index()
        TextDF.to_excel('TextMatrix.xlsx')
    return ConceptPack
