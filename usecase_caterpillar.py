import pds

def main():
    """
    Creates a random caterpillar of maximum degree 3, finds and draws a PDS of
    maximum size.
    """
    min_nb_vertices = 6
    C = pds.create_random_caterpillar(min_nb_vertices, 0.42, max_deg=3)
    max_pds = pds.find_one_max_pds(C)
    pds.draw_graph(C, max_pds, layout="spring")
    
    # Print characteristics of the caterpillar.
    nb_vertices = len(C.nodes())
    max_pds_size = pds.pds_size(len(C.nodes()), pds.max_degree(C))
    print(f"|V| = {nb_vertices}")
    print(f"|S| = {max_pds_size} (max. pds size)")
    print(f"max. pds: {max_pds}")
    
if __name__ == '__main__':
    main()