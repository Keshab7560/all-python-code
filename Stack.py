class Stack:
    def __init__(self):
        self.stack = []

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Push an item onto the stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    # Pop an item from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty."
        return self.stack.pop()

    # Peek at the top item of the stack
    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        return self.stack[-1]

    # Get the size of the stack
    def size(self):
        return len(self.stack)

    # Display the stack
    def display(self):
        print("Stack:", self.stack)


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    # Push items onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # Display the current stack
    stack.display()
    
    # Peek at the top item
    print("Top item is:", stack.peek())
    
    # Pop an item from the stack
    print("Popped item:", stack.pop())
    
    # Display the current stack after popping
    stack.display()
    
    # Check the size of the stack
    print("Stack size is:", stack.size())
    
    # Pop all items and check if the stack is empty
    stack.pop()
    stack.pop()
    print("Stack is empty:", stack.is_empty())
  
