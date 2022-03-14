import pds
import networkx as nx

# Random graph, also known as an Erdős-Rényi graph or a binomial graph.
G = nx.binomial_graph(14, 0.3)
while pds.max_degree(G) > 4:
    G = nx.binomial_graph(14, 0.3)
max_pds = pds.find_one_max_pds(G)
pds.draw_graph(G, max_pds, layout="spring")

max_degree = pds.max_degree(G)
nb_vertices = len(G.nodes())
max_pds_size = pds.pds_size(len(G.nodes()), max_degree)
print(f"delta(G) = {max_degree}")
print(f"|V| = {nb_vertices}")
print(f"|S| = {max_pds_size} (max. pds size)")
print(f"max. pds: {max_pds}")