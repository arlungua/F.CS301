import unittest
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from binary_search import BinarySearch
from find_maximum import FindMaximum
from test_data_helper import load_test_data

class TestAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data = load_test_data('test_data.txt')

    def test_insertion_sort(self):
        sorter = InsertionSort()
        input_data = self.test_data['insertion_sort']['unsorted']
        expected_sorted = self.test_data['insertion_sort']['sorted']
        sorted_data = sorter.sort(input_data.copy())
        print(f"Insertion Sort: {input_data} -> {sorted_data}")
        self.assertEqual(sorted_data, expected_sorted)

    def test_merge_sort(self):
        sorter = MergeSort()
        input_data = self.test_data['merge_sort']['unsorted']
        expected_sorted = self.test_data['merge_sort']['sorted']
        sorted_data = sorter.sort(input_data.copy())
        print(f"Merge Sort: {input_data} -> {sorted_data}")
        self.assertEqual(sorted_data, expected_sorted)

    def test_binary_search(self):
        searcher = BinarySearch()
        input_data = self.test_data['binary_search']['array']
        key = self.test_data['binary_search']['key']
        expected_result = self.test_data['binary_search']['result']
        result = searcher.search(input_data, 0, len(input_data) - 1, key)
        print(f"Binary Search: Array: {input_data}, Key: {key}, Result: {result}")
        self.assertEqual(result, expected_result)

    def test_find_maximum(self):
        finder = FindMaximum()
        input_data = self.test_data['find_maximum']['array']
        expected_value = self.test_data['find_maximum']['max_value']
        max_value = finder.find_max(input_data, 0, len(input_data) - 1)
        print(f"Find Maximum: Array: {input_data}, Maximum: {max_value}")
        self.assertEqual(max_value, expected_value)

if __name__ == '__main__':
    unittest.main()
