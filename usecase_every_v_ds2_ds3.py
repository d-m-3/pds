import pds

def check_every_v_ds2_ds3(vertices_nb, graphs_nb, ds3_nb, only_nh):
    """
    Goal: Tests the following conjecture computationally
    "Every cubic graph G = (V, E), with |V| > 8, 
    has at least one PDS S of maximum size, where d_S(u) = d_S(v) = 3 for 
    at most two vertices u, v in S".
    Execution and details: It creates random cubic graphs and tests if, 
    for every graph, there exists a PDS of maximum size and d_s(v) = 2 
    for every vertex v, except for at most `ds3_nb` vertices, where d_s(v) = 3.
    If there is no such PDS for a graph, the graph and all the PDSs of the 
    maximum size are drawn, and the program's execution is stopped. The number 
    of vertices in a graph and the number of created and tested graphs can be 
    defined. If the boolean "only_nh" is set to "True", only cubic graphs that 
    do not have a Hamiltonian cycle are considered (please notice that it 
    takes much longer).
    """
    print(f"\nCreating {graphs_nb} graphs of {vertices_nb} vertices and "
          "checking if, \nfor every graph G, there exists a PDS of the " 
          "maximum size \nand d_s(v) = 2 for every vertex v of G, "
          f"except for at most {ds3_nb} node(s), where, d_s(v) = 3 "
          "\nPlease wait...")
    for i in range(1, graphs_nb + 1):
        G = pds.get_connected_cubic_graph(vertices_nb, only_nh)
        a_pds, ds3 = pds.get_pds_every_v_ds2_and_ds3(G, ds3_nb)
        # If there is no PDS, where, for every vertex v, d_s(v) = 2
        if len(a_pds) == 0:
            pds.draw_graph(G, [])
            print("\nException: This graph has no PDS where, "
                  f"for every vertex v, d_s(v) = 2, and for at most {ds3_nb} "
                  "node(s), d_s(v) = 3.")
            # Draw all the PDSs of maximum size, for this graph.
            pds.draw_all_max_pds(G)
            break
        pds.display_progress(i, graphs_nb)

def main():
    # If only_nh=True, vertices_nb must be >= 10
    vertices_nb = 10
    graphs_nb = 20
    ds3_nb = 2
    check_every_v_ds2_ds3(vertices_nb, graphs_nb, ds3_nb, only_nh=True)
    
if __name__ == '__main__':
    main()