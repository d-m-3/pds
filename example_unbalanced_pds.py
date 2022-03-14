import pds
import gex

def main():
    """
    This file shows and draws a specific cubic graph on 18 vertices with
    a PDS that has not the same number of vertices in independent sets
    X and Y, expressed here as an "unbalanced PDS", which is unusual.
    """
    G = gex.G_cubic_bipartite_unbalanced_pds()
    subgraph = [0, 1, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17]
    is_sub_a_pds = pds.is_subgraph_a_pds(G, subgraph)
    print("Is subgraph", subgraph, "a PDS?", is_sub_a_pds)
    if is_sub_a_pds:
        pds.draw_graph(G, subgraph, layout="bipartite")    
    #pds.draw_all_max_pds(G, layout="bipartite")
    
if __name__ == '__main__':
    main()