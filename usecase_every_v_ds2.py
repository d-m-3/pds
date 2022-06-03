import pds


def check_every_v_ds2(vertices_nb, graphs_nb, only_nh):
    """
    Goal: Tests the following conjecture computationally 
    "Every cubic graph G = (V, E), with |V| > 8, 
    has at least one PDS S of maximum size, where d_S(u) = 2 for every 
    vertex u in V". This conjecture was proven to be wrong by the finding 
    of counterexamples.
    Execution and details: It creates random cubic graphs and tests if, 
    for every graph, there exists a PDS of maximum size and d_s(v) = 2 
    for every vertex v. If there is no such PDS for a graph, the graph and 
    all the PDSs of maximum size are drawn, and the program's execution is 
    stopped. The number of vertices in a graph and the number of created and 
    tested graphs can be defined. If the boolean "only_nh" is set to "True", 
    only cubic graphs that do not have a Hamiltonian cycle are considered 
    (please notice that it takes much longer).
    """
    print(f"\nCreating {graphs_nb} graphs of {vertices_nb} vertices and "
          "checking if, \nfor every graph G, there exists a PDS of the " 
          "maximum size \nand d_s(v) = 2 for every vertex v of G. "
          "\nPlease wait...")
    for i in range(1, graphs_nb + 1):
        G = pds.get_connected_cubic_graph(vertices_nb, only_nh)
        pds_v_ds2 = pds.get_pds_every_v_ds2(G)
        # If there is no PDS, where, for every vertex v, d_s(v) = 2
        if len(pds_v_ds2) == 0:
            pds.draw_graph(G, [])
            print("\nException: This graph has no PDS where d_s(v) = 2, "
                  "for every vertex v.")
            # Draw all the PDSs of maximum size, for this graph.
            pds.draw_all_max_pds(G)
            break
        pds.display_progress(i, graphs_nb)

def main():
    # If only_nh=True, vertices_nb must be >= 10
    vertices_nb = 10
    graphs_nb = 20
    check_every_v_ds2(vertices_nb, graphs_nb, only_nh=True)
    
if __name__ == '__main__':
    main()