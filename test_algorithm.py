import networkx as nx
import pds


def pds_k_regular_bipartite_algorithm(BG):
    """
    Returns a PDS of the maximum size. Algorithm 26.10.2021.
    """
    X = {n for n, d in BG.nodes(data=True) if d["bipartite"] == 0}
    Y = set(BG) - X
    pds_bar = _get_pair_with_one_common_neighbor(BG, X)
    
    if len(pds_bar) == 0:
        pds_bar = _get_pair_with_one_common_neighbor(BG, Y)
        if len(pds_bar) == 0:
            pds.draw_graph(BG, [], bipartite_layout=True)
            raise ValueError("No pair (u, v_X in X, with only 1 common neighbor.")
    print(pds_bar)
    
    # pds_list = V - pds_bar.
    pds_list = [v for v in list(BG.nodes) if v not in pds_bar]
     
    # UNFINISHED.
    while len(pds_list) != pds.pds_size(BG.number_of_nodes(), BG.degree[0]):
        # Set of neighbors of pds_bar other than u, v_X, v_Y
        set_neigh = []
        for s in pds_bar:
            set_neigh += list(BG.neighbors(s))
        set_neigh = set(set_neigh)
        set_neigh.difference_update(pds_bar)
        print("neigh uvxvy", list(set_neigh))
        
        removed = False
        for v4 in set_neigh:
            neighbors_v4 = set(list(BG.neighbors(v4)))
            neighbors_v4.difference_update(pds_bar)
            print("N(v4)", v4, neighbors_v4)
            # Neighbors of the neighbors of v4.
            for nv4 in neighbors_v4:
                ns_ns_v4 = set(list(BG.neighbors(nv4)))
                print(nv4, list(ns_ns_v4))
                ns_ns_v4.difference_update(pds_bar)
                ns_ns_v4.difference_update([v4])
                print(nv4, list(ns_ns_v4))
                if len(list(ns_ns_v4)) <= 1:
                    removed = False
                    break
                else:
                    removed = True
            if removed:
                pds_list.remove(v4)
                pds_bar.append(v4)
                print(v4, "removed")
                removed = True
                break
    return pds_list


# DOES NOT WORK ALWAYS
def _get_pair_with_one_common_neighbor(BG, X_or_Y):
    # Vertices not included in the PDS.
    pds_bar = []
    for u in list(X_or_Y):
        # First neighbor of u in Y.
        v_Y = list(BG.neighbors(u))[0] 
        neighbors_v_Y = list(BG.neighbors(v_Y))
        # Remove u from v_Y.
        neighbors_v_Y.remove(u)
        for v_X in neighbors_v_Y:
            if len(sorted(nx.common_neighbors(BG, u, v_X))) == 1:
                # u and v_Y have only v_Y as a common neighbor.
                # Add u, v_X, v_Y in pds_bar.
                pds_bar = [u, v_X, v_Y]
                break
        break
    return pds_bar
    

def main():
    n = 12
    k = 3
    # Algorithm 26.10.2021. DOES NOT WORK.
    BG = pds.get_k_regular_bipartite_graph(n, k)
    pds_list = pds_k_regular_bipartite_algorithm(BG)
    pds.draw_graph(BG, pds_list, bipartite_layout=True)
    is_pds = pds.is_subgraph_a_pds(BG, pds_list)
    print("is PDS?", is_pds)
    print(pds_list)

if __name__ == '__main__':
    main()