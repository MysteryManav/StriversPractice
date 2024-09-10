# Implement Stack using Linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if not self.isEmpty():
            self.head = self.head.next
        else:
            print("Stack is Empty")
    
    def Top(self):
        if not self.isEmpty():
            return self.head.data
        else:
            return -1
        
    def Size(self):
        size = 0
        temp = self.head
        while temp:
            size += 1
            temp = temp.next
        return size
    
    def isEmpty(self):
        return self.head == None
    
    def printStack(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

stack = Stack()
stack.push(6)
stack.push(3)
stack.push(7)
print(stack.Top())
print(stack.Size())
stack.pop()
print(stack.Top())
print(stack.Size())
