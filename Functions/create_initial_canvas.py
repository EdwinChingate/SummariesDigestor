import json
import networkx as nx
from pathlib import Path
from scores_metric import *
from steiner_subtree_on_tree import *
from CanvasCoordinates import *
from orient_layout_by_diameter import *
from layout_to_canvas_coords import *
from build_edges_undirected_perp import *
from LeavesOneWay import *
from branches_from_the_heart import *
from BranchExpansion import *

def create_initial_canvas(MaximumSimilarityTree,
                          QuestionsConceptsDF, 
                          MetricV=["degree"], 
                          N=20, 
                          canvas_path="initial.canvas",
                          psi=0.3, 
                          card_width=500, 
                          card_height=120, 
                          padding=50,
                          Develop=0):
    canvas_nodes=scores_metric(G=MaximumSimilarityTree, 
                               MetricV=MetricV,
                               N=N)
    canvas_nodes_tree=steiner_subtree_on_tree(G=MaximumSimilarityTree,
                                              terminals=canvas_nodes)
    spacing_x = card_width+padding
    spacing_y = card_height+padding
    nodes_json = []
    edges_json = []
    LittleTree= MaximumSimilarityTree.subgraph(canvas_nodes_tree.nodes)  # induced subgraph
    Branches_Heart_and_Leaves=branches_from_the_heart(Tree=LittleTree,
                                                      MaximumSimilarityTree=MaximumSimilarityTree)
    Leaves=Branches_Heart_and_Leaves[2]
    Heart=Branches_Heart_and_Leaves[1]
    nodes_to_render = list(LittleTree.nodes())
    pos=CanvasCoordinates(Branches_Heart_and_Leaves=Branches_Heart_and_Leaves,
                           psi=psi,
                           card_width=card_width,
                           card_height=card_height, 
                           padding=padding)
    canvas_xy=pos
    nodes_json = []  
    LeavesOnewayMatrix=LeavesOneWay(MaximumSimilarityTree=MaximumSimilarityTree,
                                    Heart=Heart,
                                    Leaves=Leaves)   

    for node in nodes_to_render:
        text = str(QuestionsConceptsDF.iloc[int(node)].name) if str(node).isdigit() else str(node)
        x, y         = canvas_xy[node]
        ExtraText=''
        if node in Leaves:            
            minL,maxL,NBranches=BranchExpansion(node=node,
                                                LeavesPathwayMatrix=LeavesOnewayMatrix)
            ExtraText='\nmin: '+str(minL)+'\tmax: '+str(maxL)+'\nBranches: '+str(NBranches)+'\nDevelop: '+str(Develop)
        if node in list(canvas_nodes):
            color='5'
        else:
            color='6'
        nodes_json.append({
            "type": "text",
            "id": str(node),
            "text":'id: '+str(node)+'\n'+ text+ExtraText,
            "x": int(x),
            "y": int(y),
            "width": card_width,
            "height": card_height,
            "color": color
        })

    edges_json =build_edges_undirected_perp(LittleTree, nodes_json, card_w=card_width, card_h=card_height)

    data = {"nodes": nodes_json, "edges": edges_json}

    Path(canvas_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
