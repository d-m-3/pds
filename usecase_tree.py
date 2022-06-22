import pds


def main():
    """
    Goal: Create a random tree of maximum degree 3, find and draw a PDS 
    of maximum size.
    """
    nb_vertices = 20
    T = pds.create_random_tree(nb_vertices, max_deg=3)
    max_pds = pds.find_one_max_pds(T)
    pds.draw_graph(T, max_pds, layout="spring")
    
    # Print characteristics of the tree.
    max_degree = pds.max_degree(T)
    nb_vertices = len(T.nodes())
    max_pds_size = pds.pds_size(len(T.nodes()), max_degree)
    print(f"delta(G) = {max_degree}")
    print(f"|V| = {nb_vertices}")
    print(f"|S| = {max_pds_size} (max. pds size)")
    print(f"max. pds: {max_pds}")
    
if __name__ == '__main__':
    main()