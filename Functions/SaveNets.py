import pandas as pd
import numpy as np
from Replace import *
from datetime import datetime
def SaveNets(Concepts_in_Pool,mapName,Links,netName):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H:%M")
    MapName=mapName+'_'+dt_string+'.csv'
    NetName=netName+'_'+dt_string+'.csv'
    ConceptsinPool=list(map(Replace,Concepts_in_Pool))
    Nconcepts=len(ConceptsinPool)
    MapDF=pd.DataFrame(np.array([np.arange(Nconcepts),np.arange(Nconcepts)]).T,index=ConceptsinPool,columns=['x','y'])
    MapDF.to_csv(MapName,index_label='id')
    NetDF=pd.DataFrame(Links)
    NetDF=NetDF.drop_duplicates()    
    NetDF.to_csv(NetName,index=False,header=False)
