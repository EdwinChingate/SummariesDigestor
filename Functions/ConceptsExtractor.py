from AllConcepts import *
def ConceptsExtractor(textName,startKey="[[",endKey="]]"):
    Text = open(textName, "r")
    TextLines=Text.readlines()
    Text.close()
    ConceptsList=AllConcepts(TextLines,startKey="[[",endKey="]]")
    return ConceptsList
