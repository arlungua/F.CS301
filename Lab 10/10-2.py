class Stack:
    def __init__(self):
        self.stack = []
        self.capacity = 1

    def push(self, item):
        if len(self.stack) >= self.capacity:
            self._resize()
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def _resize(self):
        self.capacity *= 2
        self.stack = self.stack[:len(self.stack)] 

    def size(self):
        return len(self.stack)

# Тест
stack = Stack()
for i in range(10):
    stack.push(i)
    print(f"Stack size after pushing {i}: {stack.size()}")

for i in range(5):
    stack.pop()
    print(f"Stack size after popping {i}: {stack.size()}")
