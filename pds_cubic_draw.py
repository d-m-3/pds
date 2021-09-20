import networkx as nx
import pds_cubic as pds


def main():
    vertices_nb = 28
    # Creates a random cubic graph with the number of vertices given above
    G = nx.random_regular_graph(3, vertices_nb, seed=None)
    max_pds = pds.find_max_pds(G, vertices_nb)
    pds.draw_graph(G, max_pds)
    
    # Other possible usage: Draw a previously saved graph from file.
    #draw_graph_from_file("graph.gz")

if __name__ == '__main__':
    main()