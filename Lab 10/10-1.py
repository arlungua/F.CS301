import math

def calculate_amortized_cost(n):
    k = math.floor(math.log2(n))
    total_cost = (2 ** (k+1)) - 1 + (n-(k+1))
    return total_cost, total_cost / n

n= 10 
total_cost, amortized_cost= calculate_amortized_cost(n)
print (f"Total cost (T({n}))= {total_cost}")
print (f"Amortized cost = {amortized_cost:.2f}")
