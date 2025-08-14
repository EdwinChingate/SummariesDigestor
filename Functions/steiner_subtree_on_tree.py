def steiner_subtree_on_tree(G, terminals):
    """
    Exact Steiner subtree on a tree:
    Iteratively prune leaves not in `terminals` until all leaves are terminals.
    Assumes G is connected & acyclic (a tree). Returns an induced subgraph.
    """
    T = G.copy()
    term_set = set(terminals) & set(T.nodes)
    if len(term_set) <= 1:
        return T.subgraph(term_set).copy()

    # prune non-terminal leaves
    prunable = [n for n in list(T.nodes) if T.degree(n) <= 1 and n not in term_set]
    while prunable:
        for n in prunable:
            if n in T:
                T.remove_node(n)
        prunable = [n for n in list(T.nodes) if T.degree(n) <= 1 and n not in term_set]
    return T
