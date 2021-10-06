import unittest
import networkx as nx
import pds_cubic as pds
import gex


class TestMaxPdsCubicGraphs(unittest.TestCase):

    def test_is_vertex_satisfied_in_subgraph(self):
        """
        Tests the function is_vertex_satisfied_in_subgraph.
        """
        G = nx.Graph()
        G.add_edge(0, 1)
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(1, 3)
        G.add_edge(1, 4)
        subg = [1, 2, 3]
        self.assertEqual(pds.is_vertex_satisfied_in_subgraph(subg[0], G, 
                                                             subg), True)
    def test_hamiltonian_cycle(self):
        """
        Tests the function hamiltonian_cycle.
        """
        G = gex.G_test_6()
        self.assertEqual(pds.hamiltonian_cycle(G), [0, 2, 3, 5, 4, 1])
        
        # The Petersen graph is a cubic nonhamiltonian graph
        G1 = nx.generators.small.petersen_graph()
        self.assertEqual(pds.hamiltonian_cycle(G1), None)
        
    def test_get_pds_every_v_ds2(self):
        """
        Tests the function get_pds_every_v_ds2.
        """
        G = gex.G_test_6()
        self.assertEqual(pds.get_pds_every_v_ds2(G), [0, 1, 4, 5])
               
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxPdsCubicGraphs)
    unittest.TextTestRunner(verbosity=2).run(suite)