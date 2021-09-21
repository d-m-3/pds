import networkx as nx
import pds_cubic as pds


def main():
    vertices_nb = 28
    
    # Creates a random cubic graph with the number of vertices given above,
    # and draws the graph, with the vertices of a PDS of maximum size in red.
    G = nx.random_regular_graph(3, vertices_nb, seed=None)
    max_pds = pds.find_max_pds(G, vertices_nb)
    pds.draw_graph(G, max_pds)

if __name__ == '__main__':
    main()