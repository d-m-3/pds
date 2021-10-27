import unittest
import networkx as nx
import pds
import gex


class TestMaxPdsCubicGraphs(unittest.TestCase):
    """
    Unit tests for the functions in `pds_cubic.py` (main library)
    """

    def test_find_one_max_pds(self):
        """
        Tests the function `find_one_max_pds`.
        """
        G = gex.G_test_6()
        self.assertEqual(pds.find_one_max_pds(G), [0, 1, 4, 5])
    
    def test_get_all_max_pds(self):
        """
        Tests the function `get_all_max_pds`.
        """
        G = gex.G_test_6()
        self.assertEqual(pds.get_all_max_pds(G), [[0, 1, 4, 5], [0, 2, 3, 5], 
                                                  [1, 2, 3, 4]])
    
    def test_get_combinations_of_subsets(self):
        """
        Tests the function `get_combinations_of_subsets`.
        """
        G = gex.G_test_6()
        gcs = pds.get_combinations_of_subsets(G)
        self.assertEqual(gcs, [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 5), 
                               (0, 1, 3, 4), (0, 1, 3, 5), (0, 1, 4, 5), 
                               (0, 2, 3, 4), (0, 2, 3, 5), (0, 2, 4, 5), 
                               (0, 3, 4, 5), (1, 2, 3, 4), (1, 2, 3, 5), 
                               (1, 2, 4, 5), (1, 3, 4, 5), (2, 3, 4, 5)])
    
    def test_pds_size(self):
        """
        Tests the function `pds_size`.
        """
        self.assertEqual(pds.pds_size(8, 3), 5)
        self.assertEqual(pds.pds_size(14, 3), 9)
        self.assertEqual(pds.pds_size(20, 3), 13)
        self.assertEqual(pds.pds_size(24, 5), 19)
        
    def test_is_subgraph_a_pds(self):
        """
        Tests the function `is_subgraph_a_pds`.
        """
        G = gex.G_test_6()
        self.assertEqual(pds.is_subgraph_a_pds(G, [1, 2, 3, 4]), True)
        self.assertEqual(pds.is_subgraph_a_pds(G, [0, 1, 2, 3]), False)
        
    def test_is_vertex_satisfied_in_subgraph(self):
        """
        Tests the function `is_vertex_satisfied_in_subgraph`.
        """
        G = gex.G_test_6()
        subg = [0, 1, 4, 5]
        self.assertEqual(pds.is_vertex_satisfied_in_subgraph(0, G, subg), True)
        subg = [0, 1, 2, 3]
        self.assertEqual(pds.is_vertex_satisfied_in_subgraph(3, G, subg), False)
    
    def test_deg_subgraph(self):
        """
        Tests the function `deg_subgraph`.
        """
        G = gex.G_test_6()
        subg = [0, 1, 4, 5]
        self.assertEqual(pds.deg_subgraph(0, G, subg), 2)
        subg = [0, 1, 2, 3]
        self.assertEqual(pds.deg_subgraph(3, G, subg), 1)
   
    def test_is_pds_max(self):
        """
        Tests the function `is_pds_max`.
        """
        G = gex.G_test_6()
        self.assertEqual(pds.is_pds_max(G, [0, 1, 4, 5], 6), True)
        
    def test_get_nodes_not_part_of_pds(self):
        """
        Tests the function `get_nodes_not_part_of_pds`.
        """
        G = gex.G_test_6()
        self.assertEqual(pds.get_nodes_not_part_of_pds(G), [])
        
    def test_get_pds_every_v_ds2(self):
        """
        Tests the function `get_pds_every_v_ds2`.
        """
        G = gex.G_test_6()
        self.assertEqual(pds.get_pds_every_v_ds2(G), [0, 1, 4, 5])
        G1 = gex.G_test_10()
        self.assertEqual(pds.get_pds_every_v_ds2(G1), 
                         [0, 1, 2, 3, 4, 5, 9])
        
    def test_get_pds_every_v_ds2_and_ds3(self):
        """
        Tests the function `get_pds_every_v_ds2_and_u_w_ds3`.
        """
        G = gex.G_test_10_2ds3()
        a_pds, ds3 = pds.get_pds_every_v_ds2_and_ds3(G, 2)
        self.assertEqual(a_pds, [0, 1, 2, 3, 5, 6, 7])
        self.assertEqual(ds3, 2)
        a_pds_2, ds3_2 = pds.get_pds_every_v_ds2_and_ds3(G, 1)
        self.assertEqual(a_pds_2, [])
        self.assertEqual(ds3_2, -1)
        
        G1 = gex.G_test_10()
        a_pds_3, ds3_3 = pds.get_pds_every_v_ds2_and_ds3(G1, 2)
        self.assertEqual(a_pds_3, [0, 1, 2, 3, 4, 5, 9])
        self.assertEqual(ds3_3, 0)
        
        # Test the special case where d_s = 2 for every vertex v in the PDS.
        G2 = gex.G_test_6()
        a_pds_4, ds3_4 = pds.get_pds_every_v_ds2_and_ds3(G2, 0)
        self.assertEqual(a_pds_4, [0, 1, 4, 5])
        self.assertEqual(ds3_4, 0)
        
    def test_hamiltonian_cycle(self):
        """
        Tests the function `hamiltonian_cycle`.
        """
        G = gex.G_test_6()
        self.assertEqual(pds.hamiltonian_cycle(G), [0, 2, 3, 5, 4, 1])
        
        # The Petersen graph is a cubic non-Hamiltonian graph.
        G1 = nx.generators.small.petersen_graph()
        self.assertEqual(pds.hamiltonian_cycle(G1), None)
        
    def test_get_k_regular_bipartite_graph(self):
        """
        Tests the function `get_k_regular_bipartite_graph`.
        """
        n = 18
        k = 4
        G = pds.get_k_regular_bipartite_graph(n, k)
        # Check that the graph is bipartite.
        self.assertEqual(nx.algorithms.bipartite.is_bipartite(G), True)
        # Check that every vertex has degree k.
        for v in G.nodes():
            self.assertEqual(G.degree(v), k)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxPdsCubicGraphs)
    unittest.TextTestRunner(verbosity=2).run(suite)