import pds


def create_graph(n, k):
    BG = pds.get_k_regular_bipartite_graph(n, k)
    pds.save_graph(BG, "special_graphs/3-regular-12-vertices")
    
def main():
    '''n = 12
    k = 3
    create_graph(n, k)'''
    
    BG = pds.get_graph_from_file("special_graphs/3-regular-12-vertices.gz")
    max_pds = pds.find_one_max_pds(BG)
    pds.draw_graph(BG, max_pds, bipartite_layout=True)
    pds_subgraph = [0, 1, 2, 3, 6, 7, 8, 9]
    print("Is subgraph a PDS?", pds.is_subgraph_a_pds(BG, pds_subgraph))
    for vertex in pds_subgraph:
        if pds.is_vertex_satisfied_in_subgraph(vertex, BG, pds_subgraph) == False:
            print(f"  {vertex} is not satisfied")
    
if __name__ == '__main__':
    main()