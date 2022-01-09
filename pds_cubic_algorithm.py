import pds

def pds_cubic_algorithm(G):
    """
    Returns a PDS of maximum size, in cubic graphs. 
    Algorithm 1, December 2021 (see master thesis report).
    """
    S = set(G.nodes())
    S_bar = set() # Empty set.
    T = set()
    U = set()
    v = list(G.nodes())[0] # Get random or first vertex.
    S.discard(v)
    S_bar.add(v)
    T.update(set(G.neighbors(v))) # Add neighbors of v in T.
    max_pds_size = pds.pds_size(G.number_of_nodes(), 3)
    
    # Runtime outputs.
    print("S:", S)
    print("S_bar:", S_bar)
    print("v:", v)
    print("T", T)
    print("===")
    
    #for u in list(T):
    while len(T) != 0:
        u = list(T)[0]
        print("u", u) # Runtime output.
        T.discard(u)
        A = set(G.neighbors(u))
        A.difference_update(S_bar) # A \ S_bar
        print("A", A) # Temp test.
        
        dsnu3 = [] # List of neigbhors of u, where d_S(N(u) \ S_bar) < 3.
        for a in A:
            if pds.deg_subgraph(a, G, S) != 3:
                dsnu3.append(a)
        if len(dsnu3) == 0:
            S.discard(u)
            S_bar.add(u)
            T.update(set(G.neighbors(u))) # Add neighbors of u in T.
            T.difference_update(S_bar) # T \ S_bar
            T.difference_update(U) # T \ U
        elif len(dsnu3) > 1:
            U.add(u)
        else: # There exists one neighbor of u, where d_S(N(u) \ S_bar) < 3.
            w = dsnu3[0]
            print("w", w) # Runtime output.
            B = set(G.neighbors(w))
            B.difference_update(S_bar)
            print("B", B) # Runtime output.
            dsnu3b = 0
            for b in B:
                if pds.deg_subgraph(b, G, S) != 3:
                    dsnu3b += 1
            T.discard(w)
            if len(S) - 2 >= max_pds_size and dsnu3b == 0:
                print("Both added.") # Runtime output.
                S.discard(u)
                S.discard(w)
                S_bar.add(u)
                S_bar.add(w)
                T.update(set(G.neighbors(u))) # Add neighbors of u in T.
                T.update(set(G.neighbors(w))) # Add neighbors of w in T.
                T.difference_update(S_bar) # T \ S_bar
                T.difference_update(U) # T \ U
            else:
                print("Both discarded.") # Runtime output.
                U.add(u)
                U.add(w)
                
        print("set U", U) # Runtime output.
        if len(S) == max_pds_size:
            print("return list(S)", list(S)) # Runtime output.
            print("S_bar", S_bar) # Runtime output.
            return list(S) # Returns a list containing a PDS of the max. size.
        if len(U) > max_pds_size:
            return [] # If no PDS of the max. size, returns an empty.
        if len(T) == 0:
            C = set(G.nodes())
            C.difference_update(S_bar)
            C.difference_update(U)
            v = list(C)[0]
            print("set U", U) # Runtime output.
            T.add(v)
            
    # Runtime outputs.
    print("===")
    print("S:", S)
    print("S_bar:", S_bar)
    print("T", T)
    return list(S)

def main():
    # Test.
    nb_vertices = 14
    G = pds.get_connected_cubic_graph(nb_vertices)
    max_pds = pds_cubic_algorithm(G)
    # Check that it is a PDS.
    print("Is it a PDS?", pds.is_subgraph_a_pds(G, max_pds))
    pds.draw_graph(G, max_pds)
    
if __name__ == '__main__':
    main()