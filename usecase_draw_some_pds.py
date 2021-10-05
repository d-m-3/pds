import networkx as nx
import pds_cubic as pds


def main():
    vertices_nb = 10
    pds_nb = 5
    # Creates a random cubic graph with the number of vertices given above,
    # and draws "pds_nb" of the same graph, with the vertices of PDSs of maximum 
    # size in red. Only connected and non-Hamiltonian graphs are considered.
    G = nx.random_regular_graph(3, vertices_nb, seed=None)
    while not (pds.hamiltonian_cycle(G) == None and nx.is_connected(G)):
        G = nx.random_regular_graph(3, vertices_nb, seed=None)
    all_max_pds = pds.get_all_max_pds(G)
    # Draw "pds_nb" different PDSs of the maximum size, of the same graph.
    for i in range(pds_nb):
        pds.draw_graph(G, all_max_pds[i])
    
    # Save all PDSs of the maximum size of a graph in .png files.
    '''
    for index, a_pds in enumerate(all_max_pds):
        filepath = f"all_pds_of_a_graph/{vertices_nb}-{index}"
        figure = pds.draw_graph(G, a_pds)
        pds.save_graph_and_figure(G, figure, filepath)
    '''
    

if __name__ == '__main__':
    main()