import networkx as nx
import pds

def pds_k_regular_bipartite_algorithm(BG):
    """
    Returns a PDS of the maximum size. Algorithm 26.10.2021.
    DOES NOT WORK.
    """
    X = {n for n, d in BG.nodes(data=True) if d["bipartite"] == 0}
    for u in list(X):
        # First neighbor of u in Y.
        v_Y = list(BG.neighbors(u))[0] 
        neighbors_v_Y = list(BG.neighbors(v_Y))
        # Remove u from v_Y
        neighbors_v_Y.remove(u)
        for v_X in neighbors_v_Y:
            if len(sorted(nx.common_neighbors(BG, u, v_X))) == 1:
                # u and v_Y have only v_Y as a common neighbor.
                # Add u, v_X, v_Y in \bar{PDS}
                pds_bar = [u, v_X, v_Y]
                break
    # PDS = V - pds_bar
    pds_list = [v for v in list(BG.nodes) if v not in pds_bar]
    # Look for a vertex s in PDS that has all its neighbors in PDS
    for s in pds_list:
        if len(pds_list) == pds.pds_size(BG.number_of_nodes(), BG.degree[0]):
            break
        # Check if PDS contains all vertices of neighbors of s.
        neighbors_s = list(BG.neighbors(s))
        if all(v in pds_list for v in neighbors_s):
            # We will remove one neighbor of s that has also all its
            # neighbors in PDS
            for t in neighbors_s:
                neighbors_t = list(BG.neighbors(t))
                if all(v in pds_list for v in neighbors_t):
                    #t can be removed from PDS, and appended in \bar{PDS}
                    pds_list.remove(t)
                    pds_bar.append(t)
                    print(t)
                    break
    return pds_list

def main():
    n = 18
    k = 4
    for _ in range(100):
        BG = pds.get_k_regular_bipartite_graph(n, k)
        max_pds = pds.find_one_max_pds(BG)
        if len(max_pds) == 0:
            print("Exception")
            pds.draw_graph(BG, max_pds, bipartite_layout=True)
            break
    
    # Algorithm 26.10.2021. DOES NOT WORK
    '''
    pds_list = pds_k_regular_bipartite_algorithm(BG)
    is_pds = pds.is_subgraph_a_pds(BG, pds_list)
    print("is PDS?", is_pds)
    print(pds_list)
    '''

if __name__ == '__main__':
    main()