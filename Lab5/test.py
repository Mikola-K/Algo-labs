import unittest
from ford_fulkerson import max_flow_and_min_cut 

class Test(unittest.TestCase):
    
    def test_given_examples_one(self):
        graph = [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 0, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]]

        edge_start, edge_end = 0, 5
        self.assertEqual(max_flow_and_min_cut(graph, edge_start, edge_end), 23)
    
    def test_given_examples_two(self):
        graph = [
            [0, 5, 3, 0, 0, 0],
            [0, 0, 10, 2, 0, 10],
            [0, 4, 0, 0, 14, 0],
            [0, 10, 2, 0, 0, 2],
            [0, 1, 0, 3, 5, 0],
            [0, 0, 0, 0, 0, 0]]

        edge_start, edge_end = 0, 5
        self.assertEqual(max_flow_and_min_cut(graph, edge_start, edge_end), 8)

    def test_given_examples_three(self):
        graph = [
            [0, 1, 13, 0, 7, 0],
            [0, 8, 0, 0, 0, 10],
            [0, 0, 0, 19, 0, 4],
            [0, 0, 2, 0, 2, 0],
            [0, 5, 0, 0, 15, 0],
            [0, 0, 0, 0, 0, 0]]

        edge_start, edge_end = 0, 5
        self.assertEqual(max_flow_and_min_cut(graph, edge_start, edge_end), 10)
        