import pds


def main():
    """
    Goal: Search for exceptions, i.e., search for k-regular bipartite graphs 
    on n vertices that have no PDS of maximum size, with n > 8.
    Execution and details: It creates random k-regular bipartite graphs and 
    tests if they do not have a PDS of maximum size. If such a graph with 
    no PDS of maximum size is found, it is drawn and the program's 
    execution is stopped. The number of vertices in a graph, the value of k, 
    and the number of created and tested graphs can be defined.
    """
    n = 22
    k = 4
    graphs_nb = 1000
    for i in range(1, graphs_nb + 1):
        BG = pds.get_k_regular_bipartite_graph(n, k)
        max_pds = pds.find_one_max_pds(BG)
        if len(max_pds) == 0:
            print("Exception")
            pds.draw_graph(BG, max_pds, bipartite_layout=True)
            break
        # If no exception could be found, draw the last graph with its PDS.
        pds.display_progress(i, graphs_nb)
    pds.draw_graph(BG, max_pds, bipartite_layout=True)
    
    
if __name__ == '__main__':
    main()