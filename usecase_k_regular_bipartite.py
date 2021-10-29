import pds


def main():
    n = 24
    k = 5
    G = pds.get_k_regular_bipartite_graph(n, k)
    max_pds = pds.find_one_max_pds(G)
    pds.draw_graph(G, max_pds, bipartite_layout=True)

if __name__ == '__main__':
    main()