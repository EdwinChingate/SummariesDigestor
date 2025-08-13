import networkx as nx

def compute_layout(G, layout="spring", seed=42, **kwargs):
    """
    Return {node: (x, y)} in layout space (usually ~[-1,1] or [0,1]).
    layout: 'spring' | 'kamada_kawai' | 'spectral' | 'fruchterman_reingold' | 'planar' | 'shell' | ...
    """
    if layout == "spring":
        return nx.spring_layout(G, seed=seed, **kwargs)
    if layout == "kamada_kawai":
        return nx.kamada_kawai_layout(G, **kwargs)
    if layout == "spectral":
        return nx.spectral_layout(G, **kwargs)
    if layout == "fr":
        return nx.fruchterman_reingold_layout(G, seed=seed, **kwargs)
    if layout == "planar":
        return nx.planar_layout(G, **kwargs)
    if layout == "shell":
        return nx.shell_layout(G, **kwargs)
    # fallback
    return nx.spring_layout(G, seed=seed, **kwargs)
