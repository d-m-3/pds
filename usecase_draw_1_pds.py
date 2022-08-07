import pds


def main():
    """
    Goal: Draw a cubic graph or a *k*-regular bipartite graph and show one 
    PDS of maximum possible size.
    Execution and details: It creates a random cubic graph or *k*-regular 
    bipartite graph on a given number of vertices. It finds a PDS of maximum 
    possible size, draws the graph, and colors the vertices of the PDS in red. 
    By default, a circular layout is used to place the vertices. As an option, 
    the "bipartite" layout can be used for bipartite graphs.
    """
    vertices_nb = 18
    # Cubic graph.
    G = pds.get_connected_cubic_graph(vertices_nb)
    max_pds = pds.find_one_max_pds(G)
    pds.draw_graph(G, max_pds)
    
    # k-regular bipartite graph.
    '''
    k = 3
    G = pds.get_k_regular_bipartite_graph(vertices_nb, k)
    max_pds = pds.find_one_max_pds(G)
    pds.draw_graph(G, max_pds, layout="bipartite")
    '''

if __name__ == '__main__':
    main()