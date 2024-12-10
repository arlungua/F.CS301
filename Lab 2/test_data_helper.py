def load_test_data(file_path):
    def parse_data(data_str):
        """Helper function to convert a comma-separated string inside brackets to a list of integers."""
        return [int(x) for x in data_str.strip('[]').split(',') if x.strip()]

    test_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "InsertionSort" in line:
                _, data = line.split(":")
                parts = data.split()
                unsorted_data, sorted_data = parts[0], parts[1]
                test_data['insertion_sort'] = {
                    'unsorted': parse_data(unsorted_data),
                    'sorted': parse_data(sorted_data)
                }
            elif "MergeSort" in line:
                _, data = line.split(":")
                parts = data.split()
                unsorted_data, sorted_data = parts[0], parts[1]
                test_data['merge_sort'] = {
                    'unsorted': parse_data(unsorted_data),
                    'sorted': parse_data(sorted_data)
                }
            elif "BinarySearch" in line:
                _, data = line.split(":")
                parts = data.split()
                array_data, key_data, result_data = parts[0], parts[1], parts[2]
                test_data['binary_search'] = {
                    'array': parse_data(array_data),
                    'key': int(key_data),
                    'result': int(result_data)
                }
            elif "FindMaximum" in line:
                _, data = line.split(":")
                parts = data.split()
                array_data, max_value = parts[0], parts[1]
                test_data['find_maximum'] = {
                    'array': parse_data(array_data),
                    'max_value': int(max_value)
                }
    return test_data
