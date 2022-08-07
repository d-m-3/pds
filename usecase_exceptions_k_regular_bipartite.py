import pds


def main():
    """
    Goal: Search for *k*-regular bipartite graphs *G = (V, E)* with *|V| > 8* 
    that admit no PDS of maximum possible size.
    Execution and details: It creates random *k*-regular bipartite graphs and 
    tests if they admit a PDS of maximum possible size. If a graph with no PDS 
    of maximum possible size is found, then it is drawn, saved as a .png 
    figure and as an edge list that can be imported later, and the program's 
    execution is stopped. The number of vertices in graphs and the number of 
    created and tested graphs can be defined.
    """
    n = 18
    k = 3
    graphs_nb = 100
    for i in range(1, graphs_nb + 1):
        BG = pds.get_k_regular_bipartite_graph(n, k)
        max_pds = pds.find_one_max_pds(BG)
        if len(max_pds) == 0:
            print("Exception")
            pds.draw_graph(BG, max_pds, layout="bipartite")
            break
        pds.display_progress(i, graphs_nb)
    # If no exception could be found, draw the last graph with its PDS.
    #pds.draw_graph(BG, max_pds, layout="bipartite")
    
if __name__ == '__main__':
    main()