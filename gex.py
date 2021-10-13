import networkx as nx


def Gex1():
    """
    Returns Graph exception 1 from paper.
    """
    Gexception1 = nx.Graph()
    Gexception1.add_edge(1,2)
    Gexception1.add_edge(2,3)
    Gexception1.add_edge(3,4)
    Gexception1.add_edge(4,5)
    Gexception1.add_edge(5,6)
    Gexception1.add_edge(6,7)
    Gexception1.add_edge(7,8)
    Gexception1.add_edge(8,1)
    Gexception1.add_edge(2,4)
    Gexception1.add_edge(3,5)
    Gexception1.add_edge(6,8)
    Gexception1.add_edge(7,1)
    return Gexception1

def Gex2():
    """
    Returns graph exception 1 from paper.
    """
    Gexception2 = nx.Graph()
    Gexception2.add_edge(1,2)
    Gexception2.add_edge(2,3)
    Gexception2.add_edge(3,4)
    Gexception2.add_edge(4,5)
    Gexception2.add_edge(5,6)
    Gexception2.add_edge(6,7)
    Gexception2.add_edge(7,8)
    Gexception2.add_edge(8,1)
    Gexception2.add_edge(1,6)
    Gexception2.add_edge(2,5)
    Gexception2.add_edge(3,8)
    Gexception2.add_edge(4,7)
    return Gexception2

def G_two_K4():
    """
    Returns a graph of 8 vertices, composed of two unconnected K_4, i.e.,
    complete graphs of 4 vertices.
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
    Returns a graph of 6 vertices, used for unit tests.
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
    Returns a graph of 10 vertices, used for unit tests.
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
    Returns a graph of 10 vertices, used for unit tests.
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