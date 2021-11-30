import pds


def main():
    """
    It creates a random cubic graph on a given number of vertices. It finds 
    and draws all its PDSs of the maximum size, and vertices belonging to 
    a PDS are colored in red. Alternatively, it can create a random k-regular 
    bipartite graph instead of a cubic graph. In that case, a specific layout 
    for bipartite graphs can be used.
    """
    vertices_nb = 14
    G = pds.get_k_regular_bipartite_graph(vertices_nb, 3)
    pds.draw_all_max_pds(G, bipartite_layout=True)

if __name__ == '__main__':
    main()