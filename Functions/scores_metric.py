import networkx as nx
import numpy as np

def scores_metric(G, MetricV=["degree"], N=20):
    canvas_nodes=[]
    for metric in MetricV:
        if metric == "degree":
            scores=dict(G.degree())
        elif metric == "pagerank":
            scores=nx.pagerank(G)
        elif metric == "betweenness":
            scores=nx.betweenness_centrality(G)
        else:
            raise ValueError(f"Unknown metric: {metric}")
        top_nodes=sorted(scores, key=scores.get, reverse=True)[:N]
        canvas_nodes+=top_nodes
    canvas_nodes=np.array(canvas_nodes)
    return set(canvas_nodes)
