def count_primes(n):
    if n < 2:
        return 0

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 ба 1 нь анхны тоо биш

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    
    return sum(primes)

import unittest

class TestPrimeCount(unittest.TestCase):
    
    def test_count_primes(self):
        self.assertEqual(count_primes(18), 7)  # 7 анхны тоо
        self.assertEqual(count_primes(10), 4)  # 4 анхны тоо
        self.assertEqual(count_primes(1), 0)   # 1 нь анхны тоо биш
        self.assertEqual(count_primes(2), 1)   # 1 анхны тоо
        self.assertEqual(count_primes(50), 15) # 15 анхны тоо
    
    def test_edge_cases(self):
        self.assertEqual(count_primes(0), 0)   # 0 хүртэлх анхны тоо байхгүй
        self.assertEqual(count_primes(1), 0)   # 1 хүртэлх анхны тоо байхгүй
        self.assertEqual(count_primes(2), 1)   # 2 нэг анхны тоо
        self.assertEqual(count_primes(100), 25) # 25 анхны тоо

if __name__ == "__main__":
    unittest.main()
