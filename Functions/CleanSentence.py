def CleanSentence(line,startKey=":",endKey=","):
    start=line.find(startKey)+3
    end=line.find(endKey)-1
    cleanSentence=line[start:end]
    return cleanSentence
