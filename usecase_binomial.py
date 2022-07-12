import pds
import networkx as nx


def main():
    """
    Goal: Create an Erdős-Rényi graph, also known as a binomial graph, 
    of maximum degree 3, and try to find and draw a PDS of maximum size.
    """
    nb_vertices = 14
    G = nx.binomial_graph(nb_vertices, 0.3)
    while pds.max_degree(G) > 4:
        G = nx.binomial_graph(nb_vertices, 0.3)
    max_pds = pds.find_one_max_pds(G)
    pds.draw_graph(G, max_pds, layout="spring")
    
    # Print characteristics of the Erdős-Rényi graph.
    max_degree = pds.max_degree(G)
    nb_vertices = len(G.nodes())
    max_pds_size = pds.pds_size(len(G.nodes()), max_degree)
    print(f"delta(G) = {max_degree}")
    print(f"|V| = {nb_vertices}")
    print(f"|S| = {max_pds_size} (max. pds size)")
    print(f"max. pds: {max_pds}")
    
if __name__ == '__main__':
    main()