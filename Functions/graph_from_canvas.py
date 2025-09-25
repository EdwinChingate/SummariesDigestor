import networkx as nx
from load_canvas import *
from maybe_int import *
def graph_from_canvas(canvas, cast_ids=True, undirected=True):
    CanvasDict=load_canvas(path_or_dict=canvas)
    WritingTree=nx.Graph() if undirected else nx.DiGraph()
    NodesList=CanvasDict["nodes"]
    EdgesList=CanvasDict['edges']
    for n in NodesList:
        nid = n.get("id")
        if cast_ids:        
            nid=maybe_int(nid)
        CellType=str(n.get("type"))
        if CellType=="text":
            WritingTree.add_node(
                nid,
                type=n.get("type"),
                text=n.get("text"),
                x=n.get("x"),
                y=n.get("y"),
                width=n.get("width"),
                height=n.get("height"),
                color=n.get("color"),
            )
    for e in EdgesList:
        u = e.get("fromNode")
        v = e.get("toNode")
        if cast_ids:
            u, v =maybe_int(u),maybe_int(v)
        if u not in WritingTree or v not in WritingTree or u == v:
            continue  # skip dangling or self loops
        WritingTree.add_edge(
            u, v,
            id=e.get("id"),
            fromSide=e.get("fromSide"),
            toSide=e.get("toSide"),
            toEnd=e.get("toEnd"),
        )
    return WritingTree
