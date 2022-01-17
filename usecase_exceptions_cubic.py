import pds

    
def create_graphs_and_check(vertices_nb, graphs_nb, filepath, only_nh):
    """
    Goal: Search for exceptions, i.e., search for cubic graphs on |V| vertices 
    that have no PDS of maximum size, with |V| > 8.
    Execution and details: It creates random cubic graphs and tests if they 
    do not have a PDS of maximum size. If such a graph with no PDS of the 
    maximum size is found, it is drawn, saved as a .png figure and as an edge 
    list that can be imported later, and the program's execution is stopped. 
    The number of vertices in a graph and the number of created and tested 
    graphs can be defined. If the boolean "only_nh" is set to "True", only 
    cubic graphs that do not have a Hamiltonian cycle are considered 
    (please notice that it takes much longer).
    """
    print(f"\nCreating {graphs_nb} graphs on {vertices_nb} vertices and checking"
          " \nfor graphs that have not a PDS of maximum size. Please wait...")
    for i in range(1, graphs_nb + 1):
        G = pds.get_connected_cubic_graph(vertices_nb, only_nh)
        # Try to find a PDS of maximum size.
        max_pds = pds.find_one_max_pds(G)
        # If there is no PDS of max. size, saves graph and figure, and abort.
        if not pds.is_pds_max(G, max_pds, vertices_nb):
            figure = pds.draw_graph(G, max_pds)
            pds.save_graph_and_figure(G, figure, filepath)
            print("\nEXCEPTION has been found and saved!")
            break
        pds.display_progress(i, graphs_nb)

def main():
    vertices_nb = 18
    graphs_nb = 10
    file = pds.next_valid_filepath("EXCEPTION-%s")
    create_graphs_and_check(vertices_nb, graphs_nb, file, only_nh=True)

if __name__ == '__main__':
    main()