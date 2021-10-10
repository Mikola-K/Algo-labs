import unittest
from main import heap_sort
from copy import deepcopy

class TestHeapSort(unittest.TestCase):
    def setUp(self):
        self.lst = [12,44,59,203,-4,3]
        self.sorted_in_asc = [-4,3,12,44,59,203]
        self.sorted_in_desc = [203,59,44,12,3,-4]

    def test_sorting_in_asc(self): 
        self.assertListEqual(heap_sort(deepcopy(self.lst), "asc"), self.sorted_in_asc)

    def test_sorting_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(self.lst), "desc"), self.sorted_in_desc)

    def test_sorting_asc_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(self.sorted_in_asc), "asc"), self.sorted_in_asc)

    def test_sorting_asc_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(self.sorted_in_asc), "desc"), self.sorted_in_desc)

    def test_sorting_desc_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(self.sorted_in_desc), "desc"), self.sorted_in_desc)

    def test_sorting_desc_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(self.sorted_in_desc), "asc"), self.sorted_in_asc)