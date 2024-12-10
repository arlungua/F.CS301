class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda item: item.ratio, reverse=True)
    total_value = 0.0
    for item in items:
        if capacity <= 0:
            break
        if item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.ratio * capacity
            capacity = 0
    return total_value

items = [
    Item(10, 60),
    Item(20, 100),
    Item(30, 120)
]

capacity = 50
max_value = fractional_knapsack(capacity, items)
print(f"max: {max_value}")
