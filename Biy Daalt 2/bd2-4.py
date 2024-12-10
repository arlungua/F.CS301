# Рекурсийн аргаар Factorial тооцох
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Жишээ ашиглах
n = 5
print(f"Factorial of {n} using recursion: {factorial_recursive(n)}")  # 120


# Divide-and-Conquer аргаар Factorial тооцох
def factorial_divide_conquer(n):
    if n == 0 or n == 1:
        return 1
    mid = n // 2
    left_result = factorial_divide_conquer(mid)  # Хоёрдугаар хэсэг
    right_result = factorial_divide_conquer(n - mid)  # Нөгөө хэсэг
    return left_result * right_result * n  # Хэсгүүдийг нэгтгэж үр дүн гаргана

# Жишээ ашиглах
n = 5
print(f"Factorial of {n} using divide-and-conquer: {factorial_divide_conquer(n)}")  # 120
