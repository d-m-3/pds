import pds

def get_tree_without_max_pds(vertices_nb, max_degree):
    """
    Returns a tree that does not have a PDS of maximum size.
    """
    T = pds.create_random_tree(vertices_nb, max_deg=max_degree)
    max_pds = pds.find_one_max_pds(T)
    while len(max_pds) != 0:
        T = pds.create_random_tree(vertices_nb, max_deg=max_degree)
        max_pds = pds.find_one_max_pds(T)
    return T
    
def main():
   T = get_tree_without_max_pds(20, 3)
   pds.draw_graph(T, [], layout="spring")
    
if __name__ == '__main__':
    main()