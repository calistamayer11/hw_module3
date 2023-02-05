import unittest
from hw3 import find_pairs_naive


class TestFindPairsNaive(unittest.TestCase):
    def test_find_pairs_naive(self):
        target = 7
        integer_list = [1, 2, 3, 4, 5]
        assert find_pairs_naive(integer_list, target) == {(2, 5), (3, 4)}


unittest.main()
