from AllConcepts import *
def ConceptsExtractor(textName,startKey="[[",endKey="]]"):
    Text = open(textName, "r")
    TextLines=Text.readlines()
    Text.close()
    ConceptPack=AllConcepts(TextLines,startKey="[[",endKey="]]")
    return ConceptPack
