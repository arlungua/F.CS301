def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    
    return dp[n]

# Example usage
cost1 = [10, 15, 20]
print(minCostClimbingStairs(cost1))  # Output: 15

cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost2))  # Output: 6
