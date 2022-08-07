import pds


def main():
    """
    Goal: Draw all the possible PDSs of maximum possible size for a given 
    cubic graph or *k*-regular bipartite graph.
    Execution and details: It creates a random cubic graph or *k*-regular 
    bipartite graph on a given number of vertices. It finds all the PDSs of 
    maximum possible size and draws them on different figures 
    (vertices belonging to a PDS are colored in red). By default, a circular 
    layout is used to place the vertices. As an option, the "bipartite" 
    layout can be used for bipartite graphs.
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