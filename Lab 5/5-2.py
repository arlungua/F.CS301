import sys
import io

def knapsack(W, weights, values, n):
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

W = 50
weights = [10, 20, 30]
values = [60, 100, 120]
n = len(weights)

max_value = knapsack(W, weights, values, n)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print(f"Хариу: {max_value}")
