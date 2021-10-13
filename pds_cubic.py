import os
import sys
import math
import networkx as nx
import gex
import matplotlib.pyplot as plt
from itertools import combinations


def find_one_max_pds(G):
    """
    Returns a list containing one PDS of the maximum size. The PDS may not
    be connected.
    """
    combs = get_combinations_of_subsets(G)
    # For each possible combination, check if it is a PDS. If yes, returns.
    for subset in combs:
        if is_subgraph_a_pds(G, list(subset)):
            return list(subset)
    return [] # Returns an empty list if no PDS of the max. size could be found.

def get_all_max_pds(G):
    """
    Returns a list containing all lists of PDSs of the maximum size. The PDSs
    may not be connected.
    """
    combs = get_combinations_of_subsets(G)
    all_pds = []
    for subset in combs:
        if is_subgraph_a_pds(G, list(subset)):
            all_pds.append(list(subset))
    return all_pds

def get_combinations_of_subsets(G):
    """
    Returns a list of all possible combinations of subsets (as lists) 
    of vertices of PDSs of the maximum size.
    """
    return list(combinations(range(G.number_of_nodes()), 
                             pds_size(G.number_of_nodes())))

def pds_size(vertices_nb):
    """
    Returns the maximum possible size of a PDS, according to the number of 
    vertices, in cubic graphs.
    """
    return math.floor((2 * vertices_nb + 1)/ 3)

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
    Returns True if the given vertex is satisfied in the subgraph, i.e.,
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
    Returns True if the given PDS is of the maximum size, i.e., 
    floor((2 * |V|))/3). Otherwise, returns False. For cubic graphs of
    eight vertices, three graph exceptions are not considered.
    """
    if len(max_pds) == pds_size(vertices_nb):
        return True
    else:
        if vertices_nb != 8:
            return False
        else:
            # Check for isomophism with the three graph exceptions, if |V|=8.
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
        # If a vertex is not found in any PDS of the maximum size, return false.
        if not (vertex in (item for sublist in all_pds for item in sublist)):
            nodes_not_part_of_pds.append(vertex)
    return nodes_not_part_of_pds

def get_pds_every_v_ds2(G):
    """
    Returns a list containing one PDS of the maximum size, where for every
    vertex v, d_s(v) = 2. The PDS may not be connected.
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

def get_pds_every_v_ds2_and_u_w_ds3(G):
    """
    Returns a list containing one PDS of the maximum size, where for every
    vertex v, d_s(v) = 2, except for at most two vertices u and w, 
    where d_s(u) = d_s(w) = 3. The PDS may not be connected.
    """
    all_max_pds = get_all_max_pds(G)
    for a_pds in all_max_pds:
        every_v_ds2_one_u_ds3 = True
        ds3 = 0
        for vertex in a_pds:
            if deg_subgraph(vertex, G, a_pds) != 2:
                if ds3 > 2:
                    every_v_ds2_one_u_ds3 = False
                    break
                else:
                    ds3 += 1
        if every_v_ds2_one_u_ds3 and ds3 <= 2:
            return a_pds
    return [] # Returns an empty list if no such PDS could be found.
        
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

def get_connected_cubic_graph(vertices_nb, only_nh):
    """
    Returns a random connected cubic graph, with |V| = vertices_nb, 
    and that is non-Hamiltonian if "only_nh" is True.
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

def draw_graph(G, max_pds):
    """
    Draws the graph and highlights the vertices that belong to
    a maximum size PDS, in red. Returns the drawn graph.
    """
    pos = nx.circular_layout(G) # Or use nx.spring_layout(G)
    color_dict = {}
    for vertex in max_pds:
        color_dict[vertex] = 'red'
    color_list = [color_dict.get(node, 'yellow') for node in G.nodes()]
    plt.figure(1,figsize=(12,12))
    nx.draw(G, pos, with_labels = True, font_size = 25, node_size = 1500,
            node_color=color_list, edge_color = 'g', width = 3, alpha = 0.7)
    figure = plt.gcf()
    plt.show()
    return figure

def draw_all_max_pds(G):
    """
    Draws all the PDSs of the maximum size, for the given graph G.
    """
    all_max_pds = get_all_max_pds(G)
    for a_pds in all_max_pds:
        draw_graph(G, a_pds)

def save_graph_and_figure(G, figure, filepath):
    """
    Saves the graph (as an edge list, that can be imported), and saves the
    figure of the graph, in the given filepath (path/to/file).
    The file extensions are added automatically.
    """
    figure.savefig(f"{filepath}.png")
    nx.write_edgelist(G, f"{filepath}.gz")
    
def next_valid_filepath(pattern):
    """
    Gives the next valid filename, according to the pattern. E.g., if the 
    pattern is "sample-" and the file "sample-1.png" exists, it returns
    "sample-2".
    """
    i = 1
    while os.path.exists((pattern % i) + ".png"):
        i += 1
    return pattern % i
    
def draw_graph_from_file(filepath):
    """
    Draws a previously saved graph, from "filepath", e.g., "to/graph.gz".
    """
    draw_graph(nx.read_edgelist(filepath), [])
    
def display_progress(count, total):
    """
    Displays progress in the console, for every 10% done.
    """
    percent = round(100.0 * count / float(total), 1)
    if percent % 10 == 0:
        print(f"{int(percent)}% done.")

if __name__ == '__main__':
    print("\nYou can import this module with : \"import pds_cubic\"")