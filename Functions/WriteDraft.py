from datetime import datetime
import pandas as pd
from ReadSummary import *
from ZeroDraftGenerator import *
from LinesJumpCalc import *
from WriteSentence_inDraft import *
from WriteLine import *
def WriteDraft(DraftName='Draft',SpaceParagraph=10,minSpace=2):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H:%M")
    FileName=DraftName+'-'+dt_string+'.md'
    Parameters=pd.read_csv('Parameters.csv',index_col=0)
    PoolofKnowledgeRute=Parameters['Value']['PoolofKnowledgeFolder']   
    ZeroDraft=ZeroDraftGenerator()
    SpaceLinesNorm=LinesJumpCalc(ZeroDraft)
    for (concept1,concept2,space) in zip(ZeroDraft['Concept1'],ZeroDraft['Concept2'],SpaceLinesNorm):
        conceptFile=concept1+'.md'
        textName=PoolofKnowledgeRute+'/'+conceptFile
        TextLines=ReadSummary(textName)
        WriteSentence_inDraft(FileName,TextLines,concept2,ReferenceInd='##')
        if space>minSpace:
            WriteLine('\n'*int(SpaceParagraph),FileName)
