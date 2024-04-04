from EmptySummary import *
from WriteLine import *
def WriteSummary(textName,TextLines):
    EmptySummary(textName)    
    for line in TextLines:
        WriteLine(line,textName)       
