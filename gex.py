import networkx as nx

"""
This file contains specific graphs and graphs used for unit tests.
"""


def Gex1():
    """
    Returns graph exception 1 from PDS paper, i.e. a cubic graph that does 
    not have a PDS of the maximum size.
    """
    Gexception1 = nx.Graph()
    Gexception1.add_edge(0,1)
    Gexception1.add_edge(1,2)
    Gexception1.add_edge(2,3)
    Gexception1.add_edge(3,4)
    Gexception1.add_edge(4,5)
    Gexception1.add_edge(5,6)
    Gexception1.add_edge(6,7)
    Gexception1.add_edge(7,0)
    Gexception1.add_edge(1,3)
    Gexception1.add_edge(2,4)
    Gexception1.add_edge(5,7)
    Gexception1.add_edge(6,0)
    return Gexception1

def Gex2():
    """
    Returns graph exception 2 from PDS paper, i.e. a cubic graph that does
    not have a PDS of the maximum size.
    """
    Gexception2 = nx.Graph()
    Gexception2.add_edge(0,1)
    Gexception2.add_edge(1,2)
    Gexception2.add_edge(2,3)
    Gexception2.add_edge(3,4)
    Gexception2.add_edge(4,5)
    Gexception2.add_edge(5,6)
    Gexception2.add_edge(6,7)
    Gexception2.add_edge(7,0)
    Gexception2.add_edge(0,5)
    Gexception2.add_edge(1,4)
    Gexception2.add_edge(2,7)
    Gexception2.add_edge(3,6)
    return Gexception2

def G_two_K4():
    """
    Returns a graph on 8 vertices, consisting of two unconnected complete 
    graphs on 4 vertices each.
    """
    G_two_K4 = nx.Graph()
    G_two_K4.add_edge(1,2)
    G_two_K4.add_edge(1,3)
    G_two_K4.add_edge(1,4)
    G_two_K4.add_edge(2,3)
    G_two_K4.add_edge(2,4)
    G_two_K4.add_edge(3,4)
    G_two_K4.add_edge(5,6)
    G_two_K4.add_edge(5,7)
    G_two_K4.add_edge(5,8)
    G_two_K4.add_edge(6,7)
    G_two_K4.add_edge(6,8)
    G_two_K4.add_edge(7,8)
    return G_two_K4

def G_test_6():
    """
    Returns a cubic graph on 6 vertices, used for unit tests.
    """
    G = nx.Graph()
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    G.add_edge(5, 0)
    G.add_edge(2, 0)
    G.add_edge(4, 1)
    return G

def G_test_10():
    """
    Returns a cubic graph on 10 vertices, used for unit tests.
    """
    G = nx.Graph()
    G.add_edge(0, 4)
    G.add_edge(0, 8)
    G.add_edge(0, 9)
    G.add_edge(1, 3)
    G.add_edge(1, 5)
    G.add_edge(1, 7)
    G.add_edge(2, 4)
    G.add_edge(2, 6)
    G.add_edge(2, 9)
    G.add_edge(3, 5)
    G.add_edge(3, 7)
    G.add_edge(4, 8)
    G.add_edge(5, 6)
    G.add_edge(6, 7)
    G.add_edge(8, 9)
    return G

def G_test_10_2ds3():
    """
    Returns a cubic graph on 10 vertices, used for unit tests.
    """
    G = nx.Graph()
    G.add_edge(0, 1)
    G.add_edge(0, 6)
    G.add_edge(0, 7)
    G.add_edge(1, 3)
    G.add_edge(1, 9)
    G.add_edge(2, 5)
    G.add_edge(2, 7)
    G.add_edge(2, 9)
    G.add_edge(3, 5)
    G.add_edge(3, 8)
    G.add_edge(4, 6)
    G.add_edge(4, 8)
    G.add_edge(4, 9)
    G.add_edge(5, 6)
    G.add_edge(7, 8)
    return G

def G_bipartite_10():
    """
    Returns a cubic bipartite graph on 1o vertices, used for unit tests.
    """
    G = nx.Graph()
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 3)
    G.add_edge(9, 1)
    G.add_edge(9, 3)
    G.add_edge(9, 4)
    G.add_edge(8, 2)
    G.add_edge(8, 3)
    G.add_edge(8, 5)
    G.add_edge(7, 2)
    G.add_edge(7, 4)
    G.add_edge(7, 5)
    G.add_edge(6, 1)
    G.add_edge(6, 4)
    G.add_edge(6, 5)
    return G

def G_test_12():
    """
    Returns a cubic graph on 12 vertices.
    """
    G = nx.Graph()
    G.add_edge(0, 3)
    G.add_edge(0, 4)
    G.add_edge(0, 5)
    G.add_edge(1, 5)
    G.add_edge(1, 7)
    G.add_edge(1, 9)
    G.add_edge(2, 6)
    G.add_edge(2, 7)
    G.add_edge(2, 10)
    G.add_edge(3, 4)
    G.add_edge(3, 11)
    G.add_edge(4, 11)
    G.add_edge(5, 11)
    G.add_edge(6, 8)
    G.add_edge(6, 9)
    G.add_edge(7, 8)
    G.add_edge(8, 10)
    G.add_edge(9, 10)
    return G

def G_algorithm1_failure_14():
    """
    Returns a cubic graph on 14 vertices, for which algorithm 1 does not
    return a PDS of the maximum size, starting with vertex 3.
    """
    G = nx.Graph()
    G.add_edge(0, 7)
    G.add_edge(0, 8)
    G.add_edge(0, 12)
    G.add_edge(1, 6)
    G.add_edge(1, 7)
    G.add_edge(1, 9)
    G.add_edge(2, 3)
    G.add_edge(2, 10)
    G.add_edge(2, 12)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 6)
    G.add_edge(4, 11)
    G.add_edge(5, 11)
    G.add_edge(5, 13)
    G.add_edge(6, 11)
    G.add_edge(7, 13)
    G.add_edge(8, 9)
    G.add_edge(8, 10)
    G.add_edge(9, 13)
    G.add_edge(10, 12)
    return G

def G_cubic_bipartite_unbalanced_pds():
    """
    Specific cubic graph on 18 vertices with
    PDS [0, 1, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17] that has not the 
    same number of vertices in independent sets X and Y, expressed here as 
    an "unbalanced PDS", which is unusual.
    """
    G = nx.Graph()
    G.add_edge(0, 9)
    G.add_edge(0, 10)
    G.add_edge(0, 11)
    G.add_edge(1, 9)
    G.add_edge(1, 10)
    G.add_edge(1, 11)
    G.add_edge(2, 11)
    G.add_edge(2, 12)
    G.add_edge(2, 13)
    G.add_edge(3, 10)
    G.add_edge(3, 12)
    G.add_edge(3, 14)
    G.add_edge(4, 9)
    G.add_edge(4, 12)
    G.add_edge(4, 13)
    G.add_edge(5, 15)
    G.add_edge(5, 16)
    G.add_edge(5, 17)
    G.add_edge(6, 14)
    G.add_edge(6, 15)
    G.add_edge(6, 16)
    G.add_edge(7, 14)
    G.add_edge(7, 15)
    G.add_edge(7, 17)
    G.add_edge(8, 13)
    G.add_edge(8, 16)
    G.add_edge(8, 17)
    return G