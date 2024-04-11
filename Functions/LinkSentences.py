import numpy as np
def LinkSentences(Links,links):
    Nlinks=len(links)
    for linkid1 in np.arange(Nlinks):
        link1=links[linkid1]
        for linkid2 in np.arange(linkid1+1,Nlinks):
            link2=links[linkid2]
            Links.append([link1,link2])
    return Links
