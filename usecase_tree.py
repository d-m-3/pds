import pds

# Tree
T = pds.create_random_tree(20, max_deg=3)
max_pds = pds.find_one_max_pds(T)
pds.draw_graph(T, max_pds, layout="spring")

nb_vertices = len(T.nodes())
max_pds_size = pds.pds_size(len(T.nodes()), pds.max_degree(T))
print(f"|V| = {nb_vertices}")
print(f"|S| = {max_pds_size} (max. pds size)")
print(f"max. pds: {max_pds}")