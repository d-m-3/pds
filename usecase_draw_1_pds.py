import pds_cubic as pds


def main():
    vertices_nb = 14
    # Creates a random cubic graph with the number of vertices given above,
    # and draws the graph, with the vertices of a PDS of the maximum size in red.
    # Only connected graphs are considered.
    G = pds.get_connected_cubic_graph(vertices_nb, only_nh=True)
    max_pds = pds.find_one_max_pds(G)
    pds.draw_graph(G, max_pds)

if __name__ == '__main__':
    main()