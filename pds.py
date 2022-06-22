import os
import math
import random
import gex
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

"""
Main library for computing and showing proportionally dense subgraphs (PDSs) 
of maximum size in graphs. Alternatively, the library can be used to generate random cubic graphs and k-regular bipartite graphs. Specifically, cubic graphs, k-regular bipartite graphs, and trees can be drawn along with their PDSs.
This library can be imported as a module in any Python project by using 
"import pds".
"""


def find_one_max_pds(G):
    """
    Returns a list containing one PDS of maximum size. The PDS may not
    be connected.
    """
    combs = get_combinations_of_subsets(G)
    # For each possible combination, check if it is a PDS. If yes, returns.
    for subset in combs:
        if is_subgraph_a_pds(G, list(subset)):
            return list(subset)
    return [] # Returns an empty list if no PDS of max size could be found.

def get_all_max_pds(G):
    """
    Returns a list containing all lists of PDSs of maximum size. The PDSs
    may not be connected.
    """
    combs = get_combinations_of_subsets(G)
    all_pds = []
    for subset in combs:
        if is_subgraph_a_pds(G, list(subset)):
            all_pds.append(list(subset))
    return all_pds

def max_degree(G):
    '''
    Returns the maximum degree of the graph G.
    '''
    return max(G.degree, key=lambda x: x[1])[1]

def get_combinations_of_subsets(G):
    """
    Returns a list of all possible combinations of subsets S_i (as lists) 
    of vertices, where |S_i| = maximum size of a PDS.
    """
    return list(combinations(range(0, G.number_of_nodes()), 
                             pds_size(G.number_of_nodes(), max_degree(G))))

def pds_size(vertices_nb, max_degree):
    """
    Returns maximum possible size of a PDS, according to the number of 
    vertices and the maximum degree.
    """
    return math.floor(((vertices_nb * (max_degree - 1)) + 1)/ max_degree)

def is_subgraph_a_pds(G, subgraph):
    """
    Returns True if the given subgraph is a PDS.
    """
    for vertex in subgraph:
        if is_vertex_satisfied_in_subgraph(vertex, G, subgraph) == False:
            return False
    return True

def is_vertex_satisfied_in_subgraph(vertex, G, subgraph):
    """
    Returns True if the given vertex is satisfied in the subgraph, i.e.
    the vertex satisfies the conditions to be considered in the subgraph, 
    so that the subgraph is a PDS.
    """
    deg_s_frac = deg_subgraph(vertex, G, subgraph) / (len(subgraph) - 1)
    deg_frac = G.degree(vertex) / (G.number_of_nodes() - 1)
    return deg_s_frac >= deg_frac

def deg_subgraph(vertex, G, subgraph):
    """
    Returns the degree of a vertex, in the given subgraph.
    """
    return G.subgraph(subgraph).degree(vertex)

def is_pds_max(G, max_pds, vertices_nb):
    """
    Returns True if the given PDS is of maximum size. Otherwise, 
    returns False. For cubic graphs of eight vertices, three graph exceptions 
    are not considered.
    """
    if len(max_pds) == pds_size(vertices_nb, G.degree[0]):
        return True
    else:
        if vertices_nb != 8:
            return False
        else:
            # Check for isomophism with the three graph exceptions if |V|=8.
            if not nx.is_isomorphic(G, gex.Gex1()) and not nx.is_isomorphic(G, 
            gex.Gex2()) and not nx.is_isomorphic(G, gex.G_two_K4()):
                return False
            else:
                return True
            
def get_nodes_not_part_of_pds(G):
    """
    Returns a list of vertices that are not part of at least one PDS of
    maximum size.
    """
    all_pds = get_all_max_pds(G)
    nodes_not_part_of_pds = []
    for vertex in G.nodes():
        # If a vertex is not found in any PDS of maximum size,
        # append it to the list to be returned.
        if not (vertex in (item for sublist in all_pds for item in sublist)):
            nodes_not_part_of_pds.append(vertex)
    return nodes_not_part_of_pds

def get_pds_every_v_ds2(G):
    """
    Returns a list containing one PDS of maximum size, where for every
    vertex v, d_S(v) = 2, in 3-regular (cubic) graphs. 
    The PDS may not be connected.
    """
    all_max_pds = get_all_max_pds(G)
    for a_pds in all_max_pds:
        every_v_ds2 = True
        for vertex in a_pds:
            if deg_subgraph(vertex, G, a_pds) != 2:
                every_v_ds2 = False
                break
        if every_v_ds2:
            return a_pds
    return [] # Returns an empty list if no such PDS could be found.

def get_pds_every_v_ds2_and_ds3(G, ds3_nb):
    """
    Returns a list containing one PDS of maximum size where d_S(v) = 2 for 
    every vertex v, except for at most "ds3_nb" where d_s(v) = 3,
    in cubic graphs. The PDS may be disconnected.
    """
    all_max_pds = get_all_max_pds(G)
    for a_pds in all_max_pds:
        every_v_ds2_ds3 = True
        ds3 = 0
        for vertex in a_pds:
            if deg_subgraph(vertex, G, a_pds) != 2:
                if ds3 >= ds3_nb:
                    every_v_ds2_ds3 = False
                    break
                else:
                    ds3 += 1
        if every_v_ds2_ds3 and ds3 <= ds3_nb:
            return a_pds, ds3
    return [], -1 # Returns an empty list if no such PDS could be found.
        
def hamiltonian_cycle(G):
    """
    Returns a Hamiltonian cycle if it exists.
    Adatped from https://gist.github.com/mikkelam/ab7966e7ab1c441f947b
    """
    F = [(G, [list(G.nodes())[0]])]
    n = G.number_of_nodes()
    while F:
        graph, path = F.pop()
        confs = []
        neighbors = (node for node in graph.neighbors(path[-1]) 
                     if node != path[-1]) # Exclude self loops
        for neighbor in neighbors:
            conf_p = path[:]
            conf_p.append(neighbor)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g, conf_p))
        for g, p in confs:
            if len(p) == n and G.has_edge(p[0], p[-1]):
                return p
            else:
                F.append((g, p))
    return None

def get_connected_cubic_graph(vertices_nb, only_nh=False):
    """
    Returns a random connected cubic graph with |V| = vertices_nb, 
    that is non-Hamiltonian if "only_nh" is True.
    """
    if only_nh:
        G = nx.random_regular_graph(3, vertices_nb, seed=None)
        while not (hamiltonian_cycle(G) == None and nx.is_connected(G)):
            G = nx.random_regular_graph(3, vertices_nb, seed=None)
    else:
        G = nx.random_regular_graph(3, vertices_nb, seed=None)
        while not nx.is_connected(G):
            G = nx.random_regular_graph(3, vertices_nb, seed=None)
    return G

def get_k_regular_bipartite_graph(vertices_nb, k):
    """
    Returns a random k-regular bipartite graph on "vertices_nb" of vertices.
    """
    if vertices_nb % 2 != 0:
        raise ValueError("The number of vertices must be even.")
    # Create a graph.
    G = nx.Graph()
    vertices_list = [i for i in range(0, vertices_nb)]
    X_int = vertices_list[:len(vertices_list)//2]
    Y_int = vertices_list[len(vertices_list)//2:]
    # Add the vertices in X and Y, and create sets X and Y.
    G.add_nodes_from(X_int, bipartite=0)
    G.add_nodes_from(Y_int, bipartite=1)
    X = {n for n, d in G.nodes(data=True) if d["bipartite"] == 0}
    Y = set(G) - X
    # Add k edges for every vertex in X.
    for v_X in X:
        for _ in range(0, k):
            v_Y = _get_appropriate_random_vertex_in_Y(G, Y, v_X, k)
            G.add_edge(v_X, v_Y)
    return G

def _get_appropriate_random_vertex_in_Y(G, Y, v_X, k):
    """
    Helper method to construct a k-regular bipartite graph G = (X,Y,E).
    Returns an appropriate and partly random vertex v_Y in Y for the given 
    vertex v_X in X, such that the edge v_X--v_Y can be added.
    """
    # List of vertices in Y, sorted by increasing degree.
    incr_deg_Y = sorted(G.degree(Y), key=lambda x: x[1])
    # Remove vertices in Y, if d(v) = k.
    incr_deg_Y = [(i, deg) for (i, deg) in incr_deg_Y if deg != k]
    for v_Y in incr_deg_Y:
        if G.has_edge(v_X, v_Y[0]):
            # Remove v_Y in Y's candidate list, if the edge already exists.
            incr_deg_Y.remove(v_Y)
    # Get the currently smallest degree in Y.
    smallest_deg_Y = incr_deg_Y[0][1]
    # Get only the candidates in Y that have currently the smallest degree.
    incr_deg_Y = [(i, deg) for (i, deg) in incr_deg_Y if deg == smallest_deg_Y]
    if len(incr_deg_Y) == 1:
        v_Y = incr_deg_Y[0][0]
    else:
        # If the length of the candidate's list >=2, randomly choose one.
        v_Y = random.choice(incr_deg_Y)[0]
        while G.has_edge(v_X, v_Y):
            v_Y = random.choice(incr_deg_Y)[0]
    return v_Y

def create_random_caterpillar(n, p, max_deg=10):
    '''
    Returns a random caterpillar graph with at least "n" backbone vertices, 
    and a "p" probability of adding an edge to the backbone.
    The maximum degree of the caterpillar can be given. The default maximum
    degree is 10.
    '''
    C = nx.generators.random_graphs.random_lobster(n, p, 0)
    while len(C.nodes()) < n or max_degree(C) > max_deg:
        C = nx.generators.random_graphs.random_lobster(n, p, 0)
    return C

def create_random_tree(nb_vertices, max_deg=10):
    '''
    Returns a random tree graph with "n" vertices. The maximum degree of 
    the tree can be given. The default maximum degree is 10.
    '''
    T = nx.random_tree(nb_vertices)
    while max_degree(T) > max_deg:
        T = nx.random_tree(nb_vertices)
    return T
    
def draw_graph(G, max_pds, layout="circular"):
    """
    Draws the graph and highlights in red the vertices that belong to
    a PDS of maximum size and returns the drawn graph.
    By default, ciruclar layout is used. 
    Bipartite and spring layouts can be used as an option.
    """
    if layout == "bipartite":
        X = nx.algorithms.bipartite.sets(G)[0]
        pos = nx.drawing.layout.bipartite_layout(G, X)
    elif layout == "spring":
        pos = nx.spring_layout(G, seed=0)
    else: # Circular.
        pos = nx.circular_layout(G)
    color_dict = {}
    for vertex in max_pds:
        color_dict[vertex] = 'red'
    color_list = [color_dict.get(node, 'yellow') for node in G.nodes()]
    plt.figure(1,figsize=(12,12))
    nx.draw(G, pos, with_labels = True, font_size = 30, node_size = 2000,
            node_color=color_list, edge_color = 'g', width = 3, alpha = 0.7)
    figure = plt.gcf()
    plt.show()
    return figure

def draw_all_max_pds(G, layout="circular"):
    """
    Draws all the PDSs of maximum size for the given graph G.
    By default, ciruclar layout is used. 
    Bipartite and spring layouts can be used as an option.
    """
    all_max_pds = get_all_max_pds(G)
    for a_pds in all_max_pds:
        draw_graph(G, a_pds, layout)
        
def save_graph(G, filepath):
    """
    Saves the graph as an edge list that can be imported later, to the 
    given filepath (path/to/file). The file extension is added automatically.
    """
    nx.write_edgelist(G, f"{filepath}.gz", data=False)

def save_graph_and_figure(G, figure, filepath):
    """
    Saves the graph as an edge list that can be imported and saves the
    figure of the graph to the given filepath (path/to/file).
    The file extensions are added automatically.
    """
    figure.savefig(f"{filepath}.png")
    nx.write_edgelist(G, f"{filepath}.gz", data=False)
    
def next_valid_filepath(pattern):
    """
    Gives the next valid filename according to the pattern, e.g. returns
    "sample-2" if the pattern is "sample-" and the file "sample-1.png" exists.
    """
    i = 1
    while os.path.exists((pattern % i) + ".png"):
        i += 1
    return pattern % i
    
def get_graph_from_file(filepath):
    """
    Returns the graph from "filepath".
    """
    return nx.read_edgelist(filepath, nodetype=int)
    
def display_progress(count, total):
    """
    Displays progress in the console by 10% increments.
    """
    percent = round(100.0 * count / float(total), 1)
    if percent % 10 == 0:
        print(f"{int(percent)}% done.")

if __name__ == '__main__':
    print("\nYou can import this module with: \"import pds\"")