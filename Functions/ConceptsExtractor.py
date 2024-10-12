from AllConcepts import *
from ReadSummary import *
from FillingTextDF import *
def ConceptsExtractor(textName,startKey="[[",endKey="]]",WriteDF=True,Write=True, ReturnConceptPack=True):
    TextLines=ReadSummary(textName)
    ConceptPack=AllConcepts(TextLines,textName,startKey,endKey,Write)
    linesNumber=ConceptPack[2]
    ConceptsList=ConceptPack[1]
    ConceptsDB=ConceptPack[0]
    TextDF=FillingTextDF(ConceptsDB,ConceptsList,linesNumber)
    TextDF=TextDF.sort_index()    
    if WriteDF:
        TextDF.to_excel('TextMatrix.xlsx')
    if ReturnConceptPack:
        return ConceptPack
    else:
        return TextDF
