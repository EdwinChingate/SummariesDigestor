import numpy as np
import pandas as pd
import datetime

def FirstEntryLogFile(LittleTree,MaximumSimilarityTree,routeLog,Fraction_of_Questions=0.2):
    raw_cards=len(list(LittleTree.nodes()))
    N_total_cards=len(list(MaximumSimilarityTree.nodes()))
    target_cards=raw_cards*Fraction_of_Questions
    current_cards_layer=raw_cards
    current_cards=current_cards_layer
    remaining_cards=N_total_cards-current_cards
    progress=current_cards/N_total_cards*100
    Time=datetime.datetime.now()
    Date=str(Time.date())
    Hour=str(Time.timetuple()[3])
    Minute=str(Time.timetuple()[4])
    Clock=Hour+':'+Minute
    Commit=''
    StatusList=np.array([0,raw_cards,target_cards,current_cards_layer,current_cards,remaining_cards,progress,Date,Clock,Commit]).reshape(1,- 1)
    Index=[0]
    StatusDF=pd.DataFrame(StatusList,index=Index,columns=['Layer','Raw cards','Target cards','Current cards layer','Current cards','Remaining cards','Progress','Date','Time','commit'])
    StatusDF.to_excel(routeLog)
    return StatusDF
