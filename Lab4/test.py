import unittest
from dijikstra import dijkstra, Graph

class JackieTest(unittest.TestCase):
    graph = Graph()
    graph.add_node("0")
    graph.add_node("1")
    graph.add_node("4")
    graph.add_node("5")
    graph.add_node("3")
    graph.add_edge("0", "3", 8)
    graph.add_edge("1", "4", 9)
    graph.add_edge("4", "2", 4)
    graph.add_edge("5", "0", 9)
    graph.add_edge("5", "4", 6)
    graph.add_edge("5", "1", 7)
    graph.add_edge("1", "2", 1)
    graph.add_edge("3", "1", 0)
    
    def test_given_examples(self):
        self.assertEqual(dijkstra(self.graph, "5"), 9.4)
       