import pds


def check_every_v_in_pds(vertices_nb, graphs_nb, only_nh):
    """
    It creates random cubic graphs and tests if, for every graph, every vertex
    is part of at least one PDS of maximum size. If the program finds a 
    graph in which there are vertices that are not part of any PDS, the graph 
    is drawn, the vertices that are not part of any PDS are displayed, and 
    the program's execution is stopped. The number of vertices in a graph and 
    the number of created and tested graphs can be defined. If the boolean 
    "only_nh" is set to "True", only cubic graphs that do not have a 
    Hamiltonian cycle are considered (please notice that it takes much longer).
    """
    print(f"\nCreating {graphs_nb} graphs of {vertices_nb} vertices and"
          " checking if \nevery vertex of the graph is part of at least one"
          " PDS of maximum size. \nPlease wait...")
    for i in range(1, graphs_nb + 1):
        G = pds.get_connected_cubic_graph(vertices_nb, only_nh)
        nodes_not_in_pds = pds.get_nodes_not_part_of_pds(G)
        if len(nodes_not_in_pds) != 0:
            pds.draw_graph(G, [])
            print(f"These nodes are not part of a PDS: {nodes_not_in_pds}")
            break
        pds.display_progress(i, graphs_nb)

def main():
    # If only_nh=True, vertices_nb must be >= 10
    vertices_nb = 18
    graphs_nb = 500
    check_every_v_in_pds(vertices_nb, graphs_nb, only_nh=False) 

if __name__ == '__main__':
    main()