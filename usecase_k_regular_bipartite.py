import pds


def main():
    n = 12
    k = 4
    
    # Draw a k-regular bipartite graph with its PDS of the maximum size.
    '''
    BG = pds.get_k_regular_bipartite_graph(n, k)
    max_pds = pds.find_one_max_pds(BG)
    pds.draw_graph(BG, max_pds, bipartite_layout=True)
    '''
    
    # Trying to find a graph that has not a PDS of the maximum size.
    graphs_nb = 100
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