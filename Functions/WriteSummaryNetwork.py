import os
from datetime import datetime
def WriteSummaryNetwork(ConceptsList,ConceptsDF,TextName):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H:%M")    
    home=os.getcwd()
    TxtName=TextName.replace('.md','')
    FileName=home+'/Networks/SummaryNet_'+TxtName+'_'+dt_string+'.csv'
    FirstLine='Source,Target,Weight\n'
    Net=open(FileName,'w')
    Net.write(FirstLine)
    Net.close()
    for concept1 in ConceptsList:
        ConceptsLoc=ConceptsDF[concept1]>0
        Concepts=ConceptsDF[ConceptsLoc].index
        for concept2 in Concepts:
            Line_to_write=concept1+','+concept2+','+str(ConceptsDF[concept1][concept2])+'\n'
            with open(FileName,'a') as network:
                network.write(Line_to_write)
            network.close() 
