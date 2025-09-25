from graph_from_canvas import *
from tables_from_canvas import *
from load_canvas import *
def reconstruct_network_from_canvas(path_or_dict, cast_ids=True, undirected=True):
    CanvasDict=load_canvas(path_or_dict=path_or_dict)
    WritingTree=graph_from_canvas(canvas=CanvasDict,
                                  cast_ids=cast_ids,
                                  undirected=undirected)
    nodes_df, edges_df,nframes_df=tables_from_canvas(canvas=CanvasDict,
                                                     cast_ids=cast_ids)
    return WritingTree,nodes_df,edges_df,CanvasDict,nframes_df
