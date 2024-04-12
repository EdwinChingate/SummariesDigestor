def ExtractYLoc(line,startKey=":"):
    start=line.find(startKey)+2
    yLoc=float(line[start:])
    return yLoc
