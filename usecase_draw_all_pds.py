import pds


def main():
    """
    Goal: Draw all the possible PDSs of maximum possible size for a given 
    cubic graph or k-regular bipartite graph.
    Execution and details: It creates a random cubic graph on a given number 
    of vertices. It finds all its PDSs of maximum possible size and draws all 
    the different PDSs on different figures (vertices belonging to a PDS are 
    colored in red). Alternatively, it can create a random k-regular bipartite 
    graph instead of a cubic graph. In that case, a specific layout for 
    bipartite graphs can be used.
    """   
    vertices_nb = 12
    # Cubic graph.
    G = pds.get_connected_cubic_graph(vertices_nb)
    pds.draw_all_max_pds(G)
    
    # k-regular bipartite graph.
    '''
    k = 3
    G = pds.get_k_regular_bipartite_graph(vertices_nb, k)
    pds.draw_all_max_pds(G, layout="bipartite")
    '''

if __name__ == '__main__':
    main()