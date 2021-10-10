import unittest
from main import Deque 
from collections import deque

class DequeueTest(unittest.TestCase):
    def test_insert_left(self):
        test_deque = Deque()
        test_deque.insert_left(5)
        test_deque.insert_left(10)
        test_deque.insert_left(20)
        test_deque.insert_left(-13)
        test_deque.insert_left(7)

        test_deque_list = test_deque.deque_to_list()

        correct_deque = deque()
        correct_deque.appendleft(5)
        correct_deque.appendleft(10)
        correct_deque.appendleft(20)
        correct_deque.appendleft(-13)
        correct_deque.appendleft(7)

        correct_deque_list = list(correct_deque)

        self.assertEqual(test_deque_list, correct_deque_list)

    def test_insert_right(self):
        test_deque = Deque()
        test_deque.insert_right(5)
        test_deque.insert_right(10)
        test_deque.insert_right(20)
        test_deque.insert_right(-13)
        test_deque.insert_right(7)

        test_deque_list = test_deque.deque_to_list()

        correct_deque = deque()
        correct_deque.append(5)
        correct_deque.append(10)
        correct_deque.append(20)
        correct_deque.append(-13)
        correct_deque.append(7)

        correct_deque_list = list(correct_deque)

        self.assertEqual(test_deque_list, correct_deque_list)

    def test_pop_left(self):
        test_deque = Deque()
        test_deque.insert_left(1)
        test_deque.insert_left(5)
        test_deque.insert_left(7)
        test_deque.insert_left(-4)
        test_deque.pop_left()
        test_deque.pop_left()

        test_deque_list = test_deque.deque_to_list()

        correct_deque = deque()
        correct_deque.appendleft(1)
        correct_deque.appendleft(5)
        correct_deque.appendleft(7)
        correct_deque.appendleft(-4)
        correct_deque.popleft()
        correct_deque.popleft()

        correct_deque_list = list(correct_deque)

        self.assertEqual(test_deque_list, correct_deque_list)

    def test_pop_right(self):
        test_deque = Deque()
        test_deque.insert_left(1)
        test_deque.insert_left(5)
        test_deque.insert_left(7)
        test_deque.insert_left(-4)
        test_deque.pop_right()
        test_deque.pop_right()

        test_deque_list = test_deque.deque_to_list()

        correct_deque = deque()
        correct_deque.appendleft(1)
        correct_deque.appendleft(5)
        correct_deque.appendleft(7)
        correct_deque.appendleft(-4)
        correct_deque.pop()
        correct_deque.pop()

        correct_deque_list = list(correct_deque)

        self.assertEqual(test_deque_list, correct_deque_list)
    
    def test_search_by_id(self):
        test_deque = Deque()
        test_deque.insert_left(5)
        test_deque.insert_left(10)
        test_deque.insert_left(20)
        test_deque.insert_right(-13)
        test_deque.insert_right(7)
        test_data = test_deque.search_by_id(2)

        correct_deque = deque()
        correct_deque.appendleft(5)
        correct_deque.appendleft(10)
        correct_deque.appendleft(20)
        correct_deque.append(-13)
        correct_deque.append(7)
        correct_data = correct_deque[2]

        self.assertEqual(test_data, correct_data)