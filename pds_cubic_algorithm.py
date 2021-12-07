import pds

def pds_cubic_algorithm(G):
    """
    Returns a PDS of the maximum size, in cubic graphs. 
    Algorithm 1, from November 2021 (see master thesis report).
    """
    S = set(G.nodes())
    S_bar = set() # Empty set.
    T = set()
    U = set()
    v = list(G.nodes())[0] # Get random or first vertex.
    S.remove(v)
    S_bar.add(v)
    T.update(set(G.neighbors(v))) # Add neighbors of v in T.
    max_pds_size = pds.pds_size(G.number_of_nodes(), 3)
    
    # Temporary tests. To be deleted.
    print("S:", S)
    print("S_bar:", S_bar)
    print("v:", v)
    print("T", T)
    print("===")
    
    for u in list(T):
        print("u", u) # Temp test.
        T.remove(u)
        A = set(G.neighbors(u))
        A.difference_update(S_bar) # A \ S_bar
        print("A", A) # Temp test.
        
        dsnu3 = 0 # Number of neigbhors of u, where d_S(N(u) \ S_bar) < 3.
        for a in A:
            if pds.deg_subgraph(a, G, S) != 3:
                dsnu3 += 1
        if dsnu3 == 0:
            S.remove(u)
            S_bar.add(u)
            T.update(set(G.neighbors(u))) # Add neighbors of u in T.
            T.difference_update(S_bar) # T \ S_bar
            T.difference_update(U) # T \ U
        elif dsnu3 > 1:
            U.add(u)
        else: # There exists one neighbor of u, where d_S(N(u) \ S_bar) < 3.
            # TODO
            # if len(S) - 2 < max_pds_size and 
            
            
            pass
        if len(S) == max_pds_size:
            return list(S) # Returns a list containing a PDS of the max. size.
        if len(U) > max_pds_size:
            return [] # If no PDS of the max. size, returns an empty.
        if len(T) == 0:
            C = set(G.nodes())
            C.difference_update(S_bar)
            C.difference_update(U)
            v = list(C)[0]
            T.add(v)
            
    # Temporary tests. To be deleted.
    print("===")
    print("S:", S)
    print("S_bar:", S_bar)
    print("T", T)
    return S

def main():
    # Test
    G = pds.get_connected_cubic_graph(14)
    max_pds = pds_cubic_algorithm(G)
    pds.draw_graph(G, max_pds)
    
if __name__ == '__main__':
    main()
    
  
    
# ====
# Probably do not use! Increase complexity for little value.
def _nb_neighbors_dsnvertex3(G, vertex, S_bar):
    _set = set(G.neighbors(vertex))
    _set.difference_update(S_bar) # A \ S_bar
    dsn3 = 0 # Number of neigbhors of u, where d_S(N(u) \ S_bar) < 3.