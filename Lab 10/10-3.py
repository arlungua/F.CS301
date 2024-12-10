class Stack:
    def __init__(self):
        self.stack = []
        self.capacity = 1
        self.potential = 0  # Ф(Do)

    def push(self, item):
        if len(self.stack) >= self.capacity:
            self._resize()
        self.stack.append(item)
        self.potential += 1  # Ф(Di) = Ф(Do) + 1, потенциал нэмэгдэж байна

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.potential -= 1  # Ф(Di) = Ф(Do) - 1, потенциал буурч байна

    def _resize(self):
        self.capacity *= 2
        self.stack = self.stack[:len(self.stack)] 
    def size(self):
        return len(self.stack)

    def get_potential(self):
        return self.potential

# Тест
stack = Stack()
for i in range(10):
    stack.push(i)
    print(f"Stack size after pushing {i}: {stack.size()}, Potential = {stack.get_potential()}")

for i in range(5):
    stack.pop()
    print(f"Stack size after popping {i}: {stack.size()}, Potential = {stack.get_potential()}")
