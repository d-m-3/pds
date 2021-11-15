import pds
import gex


def main():
    vertices_nb = 10
    # Creates a random cubic graph with the number of vertices given above,
    # and draws all the PDSs of the maximum size, of the same graph. 
    # Only connected and non-Hamiltonian graphs are considered.
    
    #G = pds.get_connected_cubic_graph(vertices_nb, only_nh=False)
    #G = gex.G_test_12()
    G = pds.get_k_regular_bipartite_graph(vertices_nb, 3)
    pds.draw_all_max_pds(G, bipartite_layout=True)

if __name__ == '__main__':
    main()