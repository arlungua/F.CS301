def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount = amount % coin
    return count

# Example usage
coins = [25, 10, 5, 1]
amount = 63
print(coin_change(coins, amount))  # 6 
