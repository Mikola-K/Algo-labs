import unittest
from knuth_morris_pratt import kmp

class TestKnuthMorrisPratt(unittest.TestCase):
    def test_one(self):
        with open('input_tests/test_one.in', 'r') as input_file:
            data = input_file.readlines()
        search_string = data[1]
        main_string = data[0]

        self.assertEqual([2], kmp(search_string, main_string))

    def test_two(self):
        with open('input_tests/test_two.in', 'r') as input_file:
            data = input_file.readlines()
        search_string = data[1]
        main_string = data[0]

        self.assertEqual([0,7], kmp(search_string, main_string))

    def test_three(self):
        with open('input_tests/test_three.in', 'r') as input_file:
            data = input_file.readlines()
        search_string = data[1]
        main_string = data[0]

        self.assertEqual([7], kmp(search_string, main_string))