import unittest

def min_coins(coins, amount, memo):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    if amount in memo:
        return memo[amount]
    
    min_count = float('inf')
    for coin in coins:
        count = min_coins(coins, amount - coin, memo) + 1
        min_count = min(min_count, count)
    
    memo[amount] = min_count
    return min_count

def coin_change(coins, amount):
    result = min_coins(coins, amount, {})
    return result if result != float('inf') else -1
  
class TestCoinChange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3) 
        self.assertEqual(coin_change([2], 3), -1)      
        self.assertEqual(coin_change([1], 0), 0)     
        self.assertEqual(coin_change([186, 419, 83, 408], 6249), 20)

if __name__ == "__main__":
    unittest.main()
