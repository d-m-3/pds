import networkx as nx
import pds


def create_nham_cubic_graph(vertices_nb, filepath):
    """
    Creates a non-Hamiltonian cubic graph of "vertices_nb", saves it in the 
    given folder, with the given "graph_nb" at the end of the filename. It also 
    saves the figure in .png in the same directory. 
    """
    success = False
    # Tries for 50 graphs
    for i in range(50):
        # Creates a random cubic graph.
        # Looks only for connected cubic graphs.
        G = nx.random_regular_graph(3, vertices_nb, seed=None)
        while not nx.is_connected(G):
            G = nx.random_regular_graph(3, vertices_nb, seed=None)
        if pds.hamiltonian_cycle(G) == None:
            max_pds = pds.find_one_max_pds(G)
            figure = pds.draw_graph(G, max_pds)
            pds.save_graph_and_figure(G, figure, filepath)
            success = True
            print("\nSuccess, the graph and the figure have been saved.")
            break
    if not success:
        print("\nA non-Hamiltonian cubic graph could not be found. "
              "Please retry.")

def main():
    vertices_nb = 18
    file = pds.next_valid_filepath(f"non_ham_cubic_graphs/{vertices_nb}-nh-%s")
    create_nham_cubic_graph(vertices_nb, file)

if __name__ == '__main__':
    main()