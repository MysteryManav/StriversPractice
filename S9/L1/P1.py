# Implement Stack using Arrays
class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.stack = [0]*self.size
    
    def push(self, x):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = x
        else:
            print("Stack is Full")
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
        else:
            print("Stack is Empty")
    
    def Top(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            return -1
    
    def Size(self):
        return self.top + 1
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.size - 1
    
    def printStack(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])

stack = Stack()
stack.push(6)
stack.push(3)
stack.push(7)
print(stack.Top())
print(stack.Size())
stack.pop()
print(stack.Size())
print(stack.Top())
stack.printStack()
