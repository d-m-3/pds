import unittest
import networkx as nx
import pds_cubic as pds
#from tools import lecture_graph


class TestMaxPdsCubicGraphs(unittest.TestCase):

    def test_hamiltonian_cycle(self):
        """
        Tests the function hamiltonian_cycle function.
        """
        G2 = nx.Graph()
        G2.add_edge(0, 1)
        G2.add_edge(1, 2)
        G2.add_edge(2, 3)
        G2.add_edge(3, 4)
        G2.add_edge(4, 5)
        G2.add_edge(5, 0)
        G2.add_edge(2, 0)
        G2.add_edge(4, 1)
        self.assertEqual(pds.hamiltonian_cycle(G2), [0, 5, 4, 3, 2, 1])
        
        # The Petersen graph is a cubic nonhamiltonian graph
        G1 = nx.generators.small.petersen_graph()
        self.assertEqual(pds.hamiltonian_cycle(G1), None)
                     
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxPdsCubicGraphs)
    unittest.TextTestRunner(verbosity=2).run(suite)