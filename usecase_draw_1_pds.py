import pds

def main():
    """
    Goal: Draw a graph and show one PDS of maximum size.
    Execution and details: It creates a random cubic graph on a given number 
    of vertices. It finds a PDS of maximum size, draws the graph, and 
    colors the vertices of the PDS in red. Alternatively, it can create and 
    draw a random k-regular bipartite graph instead of a cubic graph. In that 
    case, a specific layout for bipartite graphs can be used.
    """
    vertices_nb = 18
    #G = pds.get_connected_cubic_graph(vertices_nb, only_nh=True)
    k = 3
    G = pds.get_k_regular_bipartite_graph(vertices_nb, k)
    max_pds = pds.find_one_max_pds(G)
    pds.draw_graph(G, max_pds, layout="bipartite")

if __name__ == '__main__':
    main()