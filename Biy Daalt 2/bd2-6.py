# Dynamic Programming аргаар Coin Change 
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Жишээ ашиглах
coins = [1, 5, 10, 25]
amount = 63
print(f"Minimum coins needed (DP): {coin_change_dp(coins, amount)}")  # 6

# Greedy аргаар Coin Change
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  
    count = 0
    for coin in coins:
        if amount == 0:
            break
        count += amount // coin  # Хамгийн том coin сонгож, дүнг хасна
        amount = amount % coin   # Үлдсэн мөнгөний дүнг тооцно

    return count if amount == 0 else -1

# Жишээ ашиглах
coins = [1, 5, 10, 25]
amount = 63
print(f"Minimum coins needed (Greedy): {coin_change_greedy(coins, amount)}")  # 6 
