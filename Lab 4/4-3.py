def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins1 = [1, 2, 5]
amount1 = 11
print(coinChange(coins1, amount1))  # Output: 3

coins2 = [2]
amount2 = 3
print(coinChange(coins2, amount2))  # Output: -1

coins3 = [1]
amount3 = 0
print(coinChange(coins3, amount3))  # Output: 0
