import pds


def check_every_v_ds2(vertices_nb, graphs_nb, only_nh):
    """
    Goal: Test the following conjecture computationally "Let *G = (V, E)* 
    be a cubic graph with *|V| > 8*. Then, there always exists a subset 
    *S subset of V* such that *G[S]* is a PDS of maximum possible size 
    and *d_S(u) = 2* for each vertex *u in S*". We proved that this conjecture 
    was false by finding counterexamples.
    Execution and details: It creates random cubic graphs and tests if, for 
    every graph, there exists at least one PDS of maximum possible size 
    such that *d_S(u) = 2* for each vertex *u* in *S*. If there is no such 
    PDS for a graph, then the graph and all the PDSs of maximum possible 
    size are drawn, and the program's execution is stopped. The number of 
    vertices in graphs and the number of created and tested graphs can be 
    defined. If the boolean "only_nh" is set to "True", then only cubic 
    graphs that do not have a Hamiltonian cycle are considered 
    (please notice that it takes much longer).
    """
    print(f"\nCreating {graphs_nb} graphs of {vertices_nb} vertices and "
          "checking if, for every graph G, there exists a PDS of the " 
          "maximum possible size and d_S(v) = 2 for every vertex v in S. "
          "\nPlease wait...")
    for i in range(1, graphs_nb + 1):
        G = pds.get_connected_cubic_graph(vertices_nb, only_nh)
        pds_v_ds2 = pds.get_pds_every_v_ds2(G)
        # If there is no PDS, where, for every vertex v, d_S(v) = 2
        if len(pds_v_ds2) == 0:
            pds.draw_graph(G, [])
            print("\nException: This graph admits no PDS of maximum possible "
                  "size such that d_S(v) = 2 for every vertex v in S. "
                  "All the PDSs of this graph are drawn.")
            # Draw all the PDSs of maximum possible size, for this graph.
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