import pds
import gex


def main():
    """
    Goal: For a given graph, draw all the possible PDSs of maximum size.
    Execution and details: It creates a random cubic graph on a given number 
    of vertices. It finds all its PDSs of maximum size and draws all the 
    different PDSs on different figures (vertices belonging to a PDS are 
    colored in red). Alternatively, it can create a random k-regular bipartite 
    graph instead of a cubic graph. In that case, a specific layout for 
    bipartite graphs can be used.
    """
    vertices_nb = 10
    G = pds.get_connected_cubic_graph(vertices_nb, only_nh=True)
    pds.draw_graph(G, [])
    pds.draw_all_max_pds(G)
    #G = gex.G_algorithm1_failure_14()
    '''
    k = 3
    G = pds.get_k_regular_bipartite_graph(vertices_nb, k)
    pds.draw_graph(G, [], layout="bipartite")
    pds.draw_all_max_pds(G, layout="bipartite")
    '''

if __name__ == '__main__':
    main()