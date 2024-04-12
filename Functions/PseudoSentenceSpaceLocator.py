import pandas as pd
def PseudoSentenceSpaceLocator(TextLines,LookForSentence='shared_name',LookForPosition='position'):
    PositionLine=[]
    NameLine=[]
    LineCount=0
    for line in TextLines:
        PositionFind=line.find(LookForPosition)
        NameFind=line.find(LookForSentence)
        if PositionFind > -1:
            PositionLine.append(LineCount)
        if NameFind > -1:
            NameLine.append(LineCount)
        LineCount+=1
    NPseudoSentence=len(PositionLine)    
    PseudoSentenceLine=NameLine[1:NPseudoSentence+1]
    LocatorDF=pd.DataFrame()
    LocatorDF['pseudoSentenceLine']=PseudoSentenceLine
    LocatorDF['positionLine']=PositionLine
    return LocatorDF
