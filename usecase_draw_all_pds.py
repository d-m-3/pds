import pds


def main():
    vertices_nb = 14
    # Creates a random cubic graph on "vertices_nb" vertices.
    #G = pds.get_connected_cubic_graph(vertices_nb, only_nh=False)
    # Creates a random k-regular bipartite graph on "vertices_nb" vertices.
    G = pds.get_k_regular_bipartite_graph(vertices_nb, 3)
    # Draws all the PDSs of the maximum size, of the given graph. 
    pds.draw_all_max_pds(G, bipartite_layout=True)

if __name__ == '__main__':
    main()