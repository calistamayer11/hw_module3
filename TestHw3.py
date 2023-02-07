import unittest
from hw3 import find_pairs_naive, find_pairs_optimized, measure_min_time


class TestFindPairsNaive(unittest.TestCase):
    def test_find_pairs_naive(self):
        target = 7
        integer_list = [1, 2, 3, 4, 5]
        assert find_pairs_naive(integer_list, target) == {(2, 5), (3, 4)}
        assert not find_pairs_naive(integer_list, target) == {(5, 2), (3, 4)}

    def test_find_pairs_optimized(self):
        target = 7
        integer_list = [1, 2, 3, 4, 5]
        assert find_pairs_optimized(integer_list, target) == {(2, 5), (3, 4)}
        assert not find_pairs_optimized(integer_list, target) == {(5, 2), (3, 4)}

    def test_measure_min_time(self):
        target = 7
        integer_list = [1, 2, 3, 4, 5]

        assert isinstance(measure_min_time(find_pairs_naive, integer_list, target), str)
        assert "." in measure_min_time(find_pairs_naive, integer_list, target)
        # converting to a float should pass
        assert isinstance(
            float(measure_min_time(find_pairs_naive, integer_list, target)), float
        )


unittest.main()
