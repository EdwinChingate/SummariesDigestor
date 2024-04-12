import pandas as pd
from CleanSentence import *
from ExtractYLoc import *
from ReadSummary import *
from PseudoSentenceSpaceLocator import *
def ZeroDraftGenerator(ProtoSentencesNetworkName='networks.js'):
    TextLines=ReadSummary(ProtoSentencesNetworkName)
    LocatorDF=PseudoSentenceSpaceLocator(TextLines,LookForSentence='shared_name',LookForPosition='position')
    SentencesLayout=[]    
    for sentenceIndex in LocatorDF.index:
        sentenceLine=LocatorDF['pseudoSentenceLine'][sentenceIndex]
        positionLine=LocatorDF['positionLine'][sentenceIndex]
        cleanSentence=CleanSentence(TextLines[sentenceLine])
        yLoc=ExtractYLoc(TextLines[positionLine+2])
        concepts=cleanSentence.split('|')
        concepts.append(yLoc)
        SentencesLayout.append(concepts)
    ZeroDraft=pd.DataFrame(SentencesLayout,columns=['Concept1','Concept2','Position'])
    ZeroDraft=ZeroDraft.sort_values(by=['Position'])
    return ZeroDraft
