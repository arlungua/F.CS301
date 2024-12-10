class BinarySearch:
    def search(self, array, low, high, key):
        if high >= low:
            mid = (high + low) // 2
            if array[mid] == key:
                return mid
            elif array[mid] > key:
                return self.search(array, low, mid - 1, key)
            else:
                return self.search(array, mid + 1, high, key)
        else:
            return -1
