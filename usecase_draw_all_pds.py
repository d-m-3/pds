import pds


def main():
    vertices_nb = 18
    # Creates a random cubic graph with the number of vertices given above,
    # and draws all the PDSs of the maximum size, of the same graph. 
    # Only connected and non-Hamiltonian graphs are considered.
    G = pds.get_connected_cubic_graph(vertices_nb, only_nh=False)
    pds.draw_all_max_pds(G)

if __name__ == '__main__':
    main()