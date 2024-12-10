def find_closest_bikes(students, bikes):
    n = len(students) 
    m = len(bikes)    
    
    result = [-1] * n  
    bike_taken = [False] * m  
    
    for student_index in range(n):
        min_distance = float('inf') 
        chosen_bike = -1  # Сонгогдсон дугуй
        
        for bike_index in range(m):
            if not bike_taken[bike_index]:
                distance = abs(students[student_index][0] - bikes[bike_index][0]) + abs(students[student_index][1] - bikes[bike_index][1])
                
                if distance < min_distance:
                    min_distance = distance
                    chosen_bike = bike_index
                elif distance == min_distance:
                    if bike_index < chosen_bike:
                        chosen_bike = bike_index

        result[student_index] = chosen_bike
        bike_taken[chosen_bike] = True 
    
    return result

# Test
import unittest

class TestClosestBikes(unittest.TestCase):
    
    def test_find_closest_bikes(self):
        self.assertEqual(find_closest_bikes([(0, 0), (1, 1)], [(0, 1), (4, 3), (2, 1)]), [0, 2])
        self.assertEqual(find_closest_bikes([(1, 1), (2, 2)], [(1, 0), (3, 2), (0, 2)]), [0, 2])
        self.assertEqual(find_closest_bikes([(0, 0)], [(1, 1), (2, 2)]), [0])
        self.assertEqual(find_closest_bikes([(1, 1)], [(2, 2), (3, 3)]), [0])

if __name__ == '__main__':
    unittest.main()
