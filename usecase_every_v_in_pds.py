import pds_cubic as pds


def check_every_v_in_pds(vertices_nb, graphs_nb, only_nh):
    """
    Creates random cubic graphs of "vertices_nb" of vertices 
    and checks if every vertex of the graph is part of at least one PDS
    of the maximum size.
    If "only_nh" is True, only cubic graphs that do not have a Hamiltonian 
    cycle are considered (note that it takes much longer).
    """
    print(f"\nCreating {graphs_nb} graphs of {vertices_nb} vertices and"
          " checking if \nevery vertex of the graph is part of at least one"
          " PDS of the maximum size. \nPlease wait...")
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
    vertices_nb = 20
    graphs_nb = 100
    check_every_v_in_pds(vertices_nb, graphs_nb, only_nh=True) 

if __name__ == '__main__':
    main()