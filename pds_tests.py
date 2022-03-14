import unittest
import networkx as nx
import pds
import gex

"""
This file contains unit tests for the functions in `pds.py` (main library).
Each "class" represents a function in `pds.py`.
"""

class TestFindOneMaxPds(unittest.TestCase):
    """
    Tests the function `find_one_max_pds`.
    """
    def test_graph1(self):
        G = gex.G_test_6()
        self.assertEqual(pds.find_one_max_pds(G), [0, 1, 4, 5])
        
    def test_graph2(self):
        G = gex.G_test_12()
        self.assertEqual(pds.find_one_max_pds(G), [0, 1, 2, 3, 4, 6, 7, 9])

class TestGetAllMaxPds(unittest.TestCase):
    """
    Tests the function `get_all_max_pds`.
    """
    def test_graph1(self):
        G = gex.G_test_6()
        self.assertEqual(pds.get_all_max_pds(G), [[0, 1, 4, 5], [0, 2, 3, 5], 
                                                  [1, 2, 3, 4]])
        
class TestMaxDegree(unittest.TestCase):  
    """
    Tests the function `max_degree`.
    """
    def test_graph1(self):
        G = gex.G_test_6()
        self.assertEqual(pds.max_degree(G), 3)
    
    def test_k_regular_bipartite_graph(self):
        G = pds.get_k_regular_bipartite_graph(12, 4)
        self.assertEqual(pds.max_degree(G), 4)
        
    def test_path_graph(self):
        G = nx.path_graph(5) # Path graph P_5
        self.assertEqual(pds.max_degree(G), 2)
    
    def test_star_graph(self):
        G = nx.star_graph(18) # Star graph K_1,18
        self.assertEqual(pds.max_degree(G), 18)
        
class TestGetCombinationsOfSubsets(unittest.TestCase): 
    """
    Tests the function `get_combinations_of_subsets`.
    """
    def test_get_combinations_of_subsets(self):
        G = gex.G_test_6()
        gcs = pds.get_combinations_of_subsets(G)
        self.assertEqual(gcs, [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 5), 
                               (0, 1, 3, 4), (0, 1, 3, 5), (0, 1, 4, 5), 
                               (0, 2, 3, 4), (0, 2, 3, 5), (0, 2, 4, 5), 
                               (0, 3, 4, 5), (1, 2, 3, 4), (1, 2, 3, 5), 
                               (1, 2, 4, 5), (1, 3, 4, 5), (2, 3, 4, 5)])

class TestPdsSize(unittest.TestCase):
    """
    Tests the function `pds_size`.
    """
    def test_pds_size1(self):
        self.assertEqual(pds.pds_size(8, 3), 5)
        
    def test_pds_size2(self):
        self.assertEqual(pds.pds_size(14, 3), 9)
        
    def test_pds_size3(self):
        self.assertEqual(pds.pds_size(20, 3), 13)
        
    def test_pds_size4(self):
        self.assertEqual(pds.pds_size(24, 3), 16)
        
    def test_pds_size5(self):
        self.assertEqual(pds.pds_size(24, 5), 19)
        
class TestIsSubgraphAPds(unittest.TestCase):
    """
    Tests the function `is_subgraph_a_pds`.
    """
    def test_graph1_True(self):
        G = gex.G_test_6()
        self.assertEqual(pds.is_subgraph_a_pds(G, [1, 2, 3, 4]), True)
    
    def test_graph1_False(self):
        G = gex.G_test_6()
        self.assertEqual(pds.is_subgraph_a_pds(G, [0, 1, 2, 3]), False)
    
    def test_graph2_True(self):
        G = gex.G_test_12()
        self.assertEqual(pds.is_subgraph_a_pds(G, [0, 1, 2, 3, 4, 6, 7, 9]),
                         True)
    
    def test_graph2_False(self):
        G = gex.G_test_12()
        self.assertEqual(pds.is_subgraph_a_pds(G, [0, 1, 2, 5, 6, 7, 8, 9]), 
                         False)
        
class TestIsVertexSatisfiedInSubgraph(unittest.TestCase):
    """
    Tests the function `is_vertex_satisfied_in_subgraph`.
    """       
    def test_graph1_True(self):
        G = gex.G_test_6()
        subg = [0, 1, 4, 5]
        self.assertEqual(pds.is_vertex_satisfied_in_subgraph(0, G, subg), True)
    
    def test_graph1_False(self):
        G = gex.G_test_6()
        sub = [0, 1, 2, 3]
        self.assertEqual(pds.is_vertex_satisfied_in_subgraph(3, G, sub), False)
    
    def test_graph2_True(self):
        G = gex.G_test_12()
        sub = [0, 1, 2, 5, 6, 7, 8, 9]
        self.assertEqual(pds.is_vertex_satisfied_in_subgraph(2, G, sub), True)
        
    def test_graph2_False(self):
        G = gex.G_test_12()
        sub = [0, 1, 2, 5, 6, 7, 8, 9]
        self.assertEqual(pds.is_vertex_satisfied_in_subgraph(0, G, sub), False)
        
class TestDegSubgraph(unittest.TestCase):
    """
    Tests the function `deg_subgraph`.
    """
    def test_graph1_v1(self):
        G = gex.G_test_6()
        subg = [0, 1, 4, 5]
        self.assertEqual(pds.deg_subgraph(0, G, subg), 2)
        
    def test_graph1_v2(self):
        G = gex.G_test_6()
        subg = [0, 1, 2, 3]
        self.assertEqual(pds.deg_subgraph(3, G, subg), 1)
    
    def test_graph2_v1(self):
        G = gex.G_test_12()
        subg = [0, 1, 2, 3, 4, 6, 7, 9]
        self.assertEqual(pds.deg_subgraph(2, G, subg), 2)
    
    def test_graph12_v2(self):
        G = gex.G_test_12()
        subg = [0, 1, 2, 3, 4, 6, 7, 9]
        self.assertEqual(pds.deg_subgraph(7, G, subg), 2)
    
class TestIsPdsMax(unittest.TestCase):
    """
    Tests the function `is_pds_max`.
    """
    def test_graph1_True(self):
        G = gex.G_test_6()
        self.assertEqual(pds.is_pds_max(G, [0, 1, 4, 5], 6), True)
        
    def test_graph2_False(self):
        G = gex.G_test_12()
        self.assertEqual(pds.is_pds_max(G, [0, 1, 2, 3, 4, 6, 7], 12), False)

class TestGetNodesNotPartOfPds(unittest.TestCase):
    """
    Tests the function `get_nodes_not_part_of_pds`.
    """
    def test_graph1(self):
        G = gex.G_test_6()
        self.assertEqual(pds.get_nodes_not_part_of_pds(G), [])
    
    def test_graph2(self):
        G = gex.G_test_12()
        self.assertEqual(pds.get_nodes_not_part_of_pds(G), [])
        
class TestGetPdsEveryVDs2(unittest.TestCase):
    """
    Tests the function `get_pds_every_v_ds2`.
    """
    def test_graph1(self):
        G = gex.G_test_6()
        self.assertEqual(pds.get_pds_every_v_ds2(G), [0, 1, 4, 5])
        
    def test_graph3(self):
        G = gex.G_test_10()
        self.assertEqual(pds.get_pds_every_v_ds2(G), 
                         [0, 1, 2, 3, 4, 5, 9])
        
class TestGetPdsEveryVDs2AndUWds3(unittest.TestCase):
    """
    Tests the function `get_pds_every_v_ds2_and_u_w_ds3`.
    """
    def test_graph3_v1(self):
        G = gex.G_test_10_2ds3()
        a_pds, ds3 = pds.get_pds_every_v_ds2_and_ds3(G, 2)
        self.assertEqual(a_pds, [0, 1, 2, 3, 5, 6, 7])
        self.assertEqual(ds3, 2)
        
    def test_graph3_v2(self):
        G = gex.G_test_10_2ds3()
        a_pds_2, ds3_2 = pds.get_pds_every_v_ds2_and_ds3(G, 1)
        self.assertEqual(a_pds_2, [])
        self.assertEqual(ds3_2, -1)
    
    def test_graph3(self):
        G = gex.G_test_10()
        a_pds_3, ds3_3 = pds.get_pds_every_v_ds2_and_ds3(G, 2)
        self.assertEqual(a_pds_3, [0, 1, 2, 3, 4, 5, 9])
        self.assertEqual(ds3_3, 0)
        
    def test_graph1(self):
        # Test the special case where d_s = 2 for every vertex v in the PDS.
        G2 = gex.G_test_6()
        a_pds_4, ds3_4 = pds.get_pds_every_v_ds2_and_ds3(G2, 0)
        self.assertEqual(a_pds_4, [0, 1, 4, 5])
        self.assertEqual(ds3_4, 0)
            
class TestHamiltonianCycle(unittest.TestCase):        
    """
    Tests the function `hamiltonian_cycle`.
    """
    def test_graph1_with_HC(self):
        G = gex.G_test_6()
        self.assertEqual(pds.hamiltonian_cycle(G), [0, 2, 3, 5, 4, 1])
    
    def test_graph2_without_HC(self):
        # The Petersen graph is a cubic non-Hamiltonian graph.
        G = nx.generators.small.petersen_graph()
        self.assertEqual(pds.hamiltonian_cycle(G), None)
       
class TestGetConnectedCubicGraph(unittest.TestCase):   
    """
    Tests the function `get_connected_cubic_graph`.
    """
    def test_different_graphs(self):
        n = 16
        # Tests for 10 different graphs.
        for graph in range(0, 10):
            G = pds.get_connected_cubic_graph(n, only_nh=False)
            # Check that every vertex has degree 3.
            for v in G.nodes():
                self.assertEqual(G.degree(v), 3)
                
    def test_hamiltonian_graph(self):
        n = 16
        # Tests for one non-Hamiltonian graphs.
        G = pds.get_connected_cubic_graph(n, only_nh=True)
        # Check that every vertex has degree 3.
        for v in G.nodes():
            self.assertEqual(G.degree(v), 3)
            
class TestGetKRegularBipartiteGraph(unittest.TestCase):
    """
    Tests the function `get_k_regular_bipartite_graph`.
    """
    def test_get_k_regular_bipartite_graph(self):
        n = 28
        k = 5
        # Tests for 20 different graphs.
        for graph in range(0, 20):
            G = pds.get_k_regular_bipartite_graph(n, k)
            # Check that the graph is bipartite.
            self.assertEqual(nx.algorithms.bipartite.is_bipartite(G), True)
            # Check that every vertex has degree k.
            for v in G.nodes():
                self.assertEqual(G.degree(v), k)
                
class TestCreateRandomCaterpillar(unittest.TestCase):
    """
    Tests the function `create_random_caterpillar`.
    """
    def test_different_caterpillars(self):
        n = 6
        deg = 5
        # Tests for 10 different graphs.
        for graph in range(0, 10):
            C = pds.create_random_caterpillar(n, 0.1, max_deg=deg)
            self.assertTrue(C.number_of_nodes() >= n) # Has at least "n" nodes
            self.assertTrue(pds.max_degree(C) <= deg) # Maximum degree
    
class TestCreateRandomTree(unittest.TestCase):
    """
    Tests the function `create_random_tree`.
    """
    def test_create_random_tree(self):
        n = 15
        deg = 5
        for graph in range(0, 10):
            T = pds.create_random_tree(n, max_deg=deg)
            self.assertTrue(T.number_of_nodes() >= n) # Has at least "n" nodes
            self.assertTrue(pds.max_degree(T) <= deg) # Maximum degree
        
if __name__ == '__main__':
    unittest.main()