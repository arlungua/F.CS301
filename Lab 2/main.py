from insertion_sort import InsertionSort
from merge_sort import MergeSort
from binary_search import BinarySearch
from find_maximum import FindMaximum

class Main:
    def __init__(self):
        self.insertion_sort = InsertionSort()
        self.merge_sort = MergeSort()
        self.binary_search = BinarySearch()
        self.find_maximum = FindMaximum()

    def execute(self):
        # Example of running the insertion sort
        A = [12, 11, 13, 5, 6]
        print("Original:", A)
        print("Sorted with Insertion Sort:", self.insertion_sort.sort(A.copy()))

        # Example of running the merge sort
        B = [38, 27, 43, 3, 9, 82, 10]
        print("Original:", B)
        print("Sorted with Merge Sort:", self.merge_sort.sort(B.copy()))

        # Example of running the binary search
        C = [2, 3, 4, 10, 40]
        key = 10
        result = self.binary_search.search(C, 0, len(C) - 1, key)
        print(f"Binary Search result for {key}:", result if result != -1 else "not found")

        # Example of running the find maximum
        D = [1, 3, 7, 8, 2, 5]
        print("Maximum value in the array:", self.find_maximum.find_max(D, 0, len(D) - 1))

if __name__ == "__main__":
    main = Main()
    main.execute()
