import pds


def main():
    # There are exceptions for n = 24, k = 5 !!!
    n = 24
    k = 3
    G = pds.get_k_regular_bipartite_graph(n, k)
    max_pds = pds.find_one_max_pds(G)
    pds.draw_graph(G, max_pds, bipartite_layout=True)
    #print(G.degree)

if __name__ == '__main__':
    main()