class FindMaximum:
    def find_max(self, array, low, high):
        if low == high:
            return array[low]
        mid = (low + high) // 2
        left_max = self.find_max(array, low, mid)
        right_max = self.find_max(array, mid + 1, high)
        return max(left_max, right_max)
