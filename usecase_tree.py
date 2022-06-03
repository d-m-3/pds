import pds

# Create a tree, find and draw a PDS.
T = pds.create_random_tree(20, max_deg=3)
max_pds = pds.find_one_max_pds(T)
pds.draw_graph(T, max_pds, layout="spring")

# Draw the tree without PDS and then all the PDSs.
'''pds.draw_graph(T, [], layout="spring")
pds.draw_all_max_pds(T, layout="spring")'''

# Print characteristics of the tree.
max_degree = pds.max_degree(T)
nb_vertices = len(T.nodes())
max_pds_size = pds.pds_size(len(T.nodes()), max_degree)
print(f"delta(G) = {max_degree}")
print(f"|V| = {nb_vertices}")
print(f"|S| = {max_pds_size} (max. pds size)")
print(f"max. pds: {max_pds}")