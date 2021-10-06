import networkx as nx
import pds_cubic as pds


def main():
    vertices_nb = 10
    # Creates a random cubic graph with the number of vertices given above,
    # and draws all the PDSs of the maximum size, of the same graph. 
    # Only connected and non-Hamiltonian graphs are considered.
    G = nx.random_regular_graph(3, vertices_nb, seed=None)
    while not (pds.hamiltonian_cycle(G) == None and nx.is_connected(G)):
        G = nx.random_regular_graph(3, vertices_nb, seed=None)
    pds.draw_all_max_pds(G)

if __name__ == '__main__':
    main()