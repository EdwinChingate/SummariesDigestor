import numpy as np
import pandas as pd
import datetime

def FirstEntryLogFile(LittleTree,MaximumSimilarityTree,routeLog,Leaves,minL_list,maxL_list,Fraction_of_Questions=0.2):
    raw_cards=len(list(LittleTree.nodes()))
    N_total_cards=len(list(MaximumSimilarityTree.nodes()))
    target_cards=raw_cards*Fraction_of_Questions
    current_cards_layer=raw_cards
    current_cards=current_cards_layer
    remaining_cards=N_total_cards-current_cards
    progress=current_cards/N_total_cards*100
    Time=datetime.datetime.now()
    Date=str(Time.date())
    hour=int(Time.timetuple()[3])
    if hour<10: #This little conditional could become a function, as I'm doing the same for hours and minutes
        Hour='0'+str(hour)
    else:
        Hour=str(hour)
    minute=int(Time.timetuple()[4])
    if minute<10:
        Minute='0'+str(minute)
    else:
        Minute=str(minute)
    Clock=Hour+':'+Minute
    Commit=''
    Comment='Tree seed'
    StatusList=np.array([0,raw_cards,target_cards,current_cards_layer,len(Leaves),len(Leaves),current_cards,remaining_cards,progress,min(minL_list),max(maxL_list),Date,Clock,Comment,Commit]).reshape(1,- 1)
    Index=[0]
    StatusDF=pd.DataFrame(StatusList,index=Index,columns=['Layer','Raw cards layer','Target cards layer','Current cards layer','Leaves','Active leaves','Current cards','Remaining cards','Progress','Min Layers','Max Layers','Date','Time','Comment','commit'])
    StatusDF.to_excel(routeLog)
    return StatusDF
