class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def reverse_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        temp_stack.push(stack.pop())
    return temp_stack

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("Original Stack:", stack)

    reversed_stack = reverse_stack(stack)
    print("Reversed Stack:", reversed_stack)