# Implement Stack using Queue
from queue import Queue

class Stack:
    def __init__(self):
        self.q = Queue()
    
    def push(self, x):
        self.q.put(x)
        for i in range(self.q.qsize() - 1):
            self.q.put(self.q.get())

    def pop(self):
        if not self.isEmpty():
            self.q.get()
        else:
            print("Stack is Empty")

    def Top(self):
        if not self.isEmpty():
            return self.q.queue[0]
        else:
            return -1
        
    def Size(self):
        return self.q.qsize()
    
    def isEmpty(self):
        return self.q.empty()
    
    def printStack(self):
        for i in range(self.q.qsize()):
            print(self.q.queue[i], end=" ")
        print()

stack = Stack()
stack.push(3)
stack.push(2)
stack.push(4)
stack.push(1)
print(stack.Top())
print(stack.Size())
stack.pop()
print(stack.Top())
print(stack.Size())
