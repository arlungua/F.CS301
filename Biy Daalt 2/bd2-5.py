# Divide-and-Conquer аргаар Fibonacci тооцох
def fibonacci_divide_conquer(n):
    if n <= 1:
        return n
    else:
        return fibonacci_divide_conquer(n-1) + fibonacci_divide_conquer(n-2)

# Жишээ ашиглах
n = 10
print(f"Fibonacci of {n} using divide-and-conquer: {fibonacci_divide_conquer(n)}")  # 55

# Dynamic Programming аргаар Fibonacci тооцох
def fibonacci_dp(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_dp(n-1, memo) + fibonacci_dp(n-2, memo)
    return memo[n]

# Жишээ ашиглах
n = 10
print(f"Fibonacci of {n} using dynamic programming: {fibonacci_dp(n)}")  # 55
