import networkx as nx
import pds_cubic as pds


def main():
    vertices_nb = 8
    # Creates a random cubic graph with the number of vertices given above,
    # and draws the graph, with the vertices of a PDS of maximum size in red.
    # Only connected graphs are considered.
    G = nx.random_regular_graph(3, vertices_nb, seed=None)
    while not nx.is_connected(G):
        G = nx.random_regular_graph(3, vertices_nb, seed=None)
    max_pds = pds.find_max_pds(G, vertices_nb)
    pds.draw_graph(G, max_pds)

if __name__ == '__main__':
    main()