import networkx as nx
import pds_cubic as pds

    
def create_graphs_and_check(vertices_nb, graphs_nb, filepath, only_nh=False):
    """
    Creates random cubic graphs of "vertices_nb" of vertices 
    and checks for graphs that have not a PDS of maximum size.
    If such a graph is found, it saves the graph (as an edge list, 
    that can be imported), and saves the figure of the graph, in the given 
    filepath (path/to/file). The file extensions are added automatically.
    If "only_nh" is True, only cubic graphs that do not have an Hamiltonian 
    cycle are considered (note that it takes much longer).
    """
    print(f"\nCreating {graphs_nb} graphs of {vertices_nb} vertices and checking"
          " \nfor graphs that have not a PDS of max. size. Please wait...")
    progress = 0
    for i in range(1, graphs_nb + 1):
        G = nx.random_regular_graph(3, vertices_nb, seed=None)
        # If only_nh == True, checks only for cubic graphs that do not have
        # an Hamiltonian cycle.
        if only_nh:
            while pds.hamiltonian_cycle(G) != None:
                G = nx.random_regular_graph(3, vertices_nb, seed=None)
        # Try to find a PDS of maximum size.
        max_pds = pds.find_max_pds(G, vertices_nb)
        # If there is no PDS of max. size, saves graph and figure, and abort.
        if not pds.is_pds_max(G, max_pds, vertices_nb):
            figure = pds.draw_graph(G, max_pds)
            pds.save_graph_and_figure(G, figure, filepath)
            print("\nEXCEPTION has been found and saved!")
            break
        if i >= ((graphs_nb / 10) + (progress * graphs_nb / 100)):
            progress += 10
            print(f"{progress}% done")

def main():
    vertices_nb = 12
    graphs_nb = 50
    file = pds.next_valid_filepath("EXCEPTION-%s")
    create_graphs_and_check(vertices_nb, graphs_nb, file, only_nh=True)

if __name__ == '__main__':
    main()