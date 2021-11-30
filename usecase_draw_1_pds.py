import pds

def main():
    vertices_nb = 14
    # Creates a random cubic graph with the number of vertices given above,
    # and draws the graph. Vertices in red form a PDS of the maximum size.
    G = pds.get_connected_cubic_graph(vertices_nb, only_nh=True)
    # Create a random k-regular bipartite graph
    #G = pds.get_k_regular_bipartite_graph(vertices_nb, 3)
    max_pds = pds.find_one_max_pds(G)
    pds.draw_graph(G, max_pds)

if __name__ == '__main__':
    main()