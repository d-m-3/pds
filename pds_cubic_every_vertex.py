import networkx as nx
import pds_cubic as pds


def check_every_vertex(vertices_nb, graphs_nb, only_nh=False):
    """
    Creates random cubic graphs of "vertices_nb" of vertices 
    and checks if every vertex of the graph is part of at least one PDS
    of maximum size.
    If "only_nh" is True, only cubic graphs that do not have a Hamiltonian 
    cycle are considered (note that it takes much longer).
    """
    print(f"\nCreating {graphs_nb} graphs of {vertices_nb} vertices and"
          " checking if \nevery vertex of the graph is part of at least one"
          " PDS of maximum size. \nPlease wait...")
    progress = 0
    for i in range(1, graphs_nb + 1):
        # If only_nh == True, checks only for connected cubic graphs that do 
        # not have an Hamiltonian cycle.
        if only_nh:
            G = nx.random_regular_graph(3, vertices_nb, seed=None)
            while not (pds.hamiltonian_cycle(G) == None and nx.is_connected(G)):
                G = nx.random_regular_graph(3, vertices_nb, seed=None)
        else:
            # Looks only for connected cubic graphs.
            G = nx.random_regular_graph(3, vertices_nb, seed=None)
            while not nx.is_connected(G):
                G = nx.random_regular_graph(3, vertices_nb, seed=None)
        nodes_not_in_pds = pds.get_nodes_not_part_of_pds(G)
        if len(nodes_not_in_pds) != 0:
            pds.draw_graph(G, [])
            print(f"These nodes are not part of a PDS: {nodes_not_in_pds}")
            break
        if i >= ((graphs_nb / 10) + (progress * graphs_nb / 100)):
            progress += 10
            print(f"{progress}% done")

def main():
    vertices_nb = 18
    graphs_nb = 20
    check_every_vertex(vertices_nb, graphs_nb, only_nh=True)

if __name__ == '__main__':
    main()