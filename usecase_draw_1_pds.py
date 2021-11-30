import pds

def main():
    """
    It creates and draws a random cubic graph on a given number of vertices. 
    It founds a PDS of the maximum size, and its vertices are colored in red. 
    Alternatively, it can create and draw a random k-regular bipartite graph 
    instead of a cubic graph. In that case, a specific layout for bipartite 
    graphs can be used.
    """
    vertices_nb = 14
    G = pds.get_connected_cubic_graph(vertices_nb, only_nh=True)
    #k = 3
    #G = pds.get_k_regular_bipartite_graph(vertices_nb, k)
    max_pds = pds.find_one_max_pds(G)
    pds.draw_graph(G, max_pds)

if __name__ == '__main__':
    main()