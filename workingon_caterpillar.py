import pds
import networkx as nx


'''
T = nx.generators.trees.random_tree(10)
max_pds = pds.find_one_max_pds(T)
pds.draw_graph(T, max_pds)
'''

# Caterpillar graph
C = pds.create_random_caterpillar(6, 0.42)
max_pds = pds.find_one_max_pds(C)
max_pds_size = pds.pds_size(len(C.nodes()), pds.max_degree(C))
nb_vertices = len(C.nodes())
print(f"|V| = {nb_vertices}")
print(f"max pds size = {max_pds_size}")
print(f"max pds: {max_pds}")
pds.draw_graph(C, max_pds, layout="spring")

'''
G = nx.generators.random_graphs.fast_gnp_random_graph(12, 0.2)
max_pds = pds.find_one_max_pds(G)
pds.draw_graph(G, max_pds, layout="spring")
'''