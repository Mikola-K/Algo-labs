import unittest
from pices import count_min_eating_time

class JackieTest(unittest.TestCase):
    def test_given_examples(self):
        self.assertEqual(count_min_eating_time([3, 6, 7, 11], 8), 4)
        self.assertEqual(count_min_eating_time([30, 11, 23, 4, 20], 6), 23)
        self.assertEqual(count_min_eating_time([30, 11, 23, 4, 20], 5), 30)

    def test_edge_cases(self):
        self.assertEqual(count_min_eating_time([30, 30, 30, 30, 30], 5), 30)
        self.assertEqual(count_min_eating_time([5, 2, 1, 3, 7], 18), 1)
        self.assertEquals(count_min_eating_time([5, 2, 1, 3, 2], 15), 1)

    def test_bad_input(self):
        self.assertRaises(ValueError, count_min_eating_time, [2, 5, 19, 84], 1)
        self.assertRaises(TypeError, count_min_eating_time, [1, 22, 41, 5, 'a'], 9)
        self.assertRaises(TypeError, count_min_eating_time, [5, 22, 4, [1, 3, 4], 7], 9)
        self.assertRaises(TypeError, count_min_eating_time, [10, 22, 4, '1', 7], 9)
        self.assertRaises(TypeError, count_min_eating_time, [2, 5, 19, 84], "15")