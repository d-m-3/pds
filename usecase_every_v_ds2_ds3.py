import pds


def check_every_v_ds2_ds3(vertices_nb, graphs_nb, ds3_nb, only_nh):
    """
    Goal: Test the following conjecture computationally "Let *G = (V, E)* 
    be a cubic graph with *|V| > 8*. Then, there always exists a subset 
    *S subset of V* such that *G[S]* is a PDS of maximum possible size 
    and *d_S(u) = 3* for at most *i* vertices *u in S* for *i > 1*".
    Execution and details: It creates random cubic graphs and tests if, 
    for every graph, there exists at least one PDS of maximum possible size 
    such that *d_S(u) = 3* for at most `ds3_nb` vertices *u in S*. If there 
    is no such PDS for a graph, then the graph and all the PDSs of maximum 
    possible size are drawn, and the program's execution is stopped. The 
    number of vertices in graphs and the number of created and tested graphs 
    can be defined. If the boolean "only_nh" is set to "True", then only 
    cubic graphs that do not have a Hamiltonian cycle are considered 
    (please notice that it takes much longer).
    """
    print(f"\nCreating {graphs_nb} graphs of {vertices_nb} vertices and "
          "checking if, \nfor every graph G, there exists a PDS of the " 
          "maximum possible size \nand d_S(v) = 2 for every vertex v of G, "
          f"except for at most {ds3_nb} node(s), where, d_S(v) = 3 "
          "\nPlease wait...")
    for i in range(1, graphs_nb + 1):
        G = pds.get_connected_cubic_graph(vertices_nb, only_nh)
        a_pds, ds3 = pds.get_pds_every_v_ds2_and_ds3(G, ds3_nb)
        if len(a_pds) == 0:
            pds.draw_graph(G, [])
            print("\nException: This graph admits no PDS of maximum possible "
                  "size such that d_S(v) = 3 "
                  f"for at most {ds3_nb} vertices v in S.")
            # Draw all the PDSs of maximum possible size, for this graph.
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