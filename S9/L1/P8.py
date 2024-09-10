# Implement Minimum Stack
# Time Complexity: O(1)
# Space Complexity: O(2n)
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        if not self.isEmpty():
            self.stack.pop()
        else:
            print("Stack is Empty")

    def Top(self):
        if not self.isEmpty():
            return self.stack[-1][0]
        else:
            return -1
        
    def getMin(self):
        if not self.isEmpty():
            return self.stack[-1][1]
        else:
            return -1
        
    def Size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return not self.stack
    
    def printStack(self):
        for i in range(len(self.stack)):
            print(self.stack[i][0], end=" ")
        print()

stack = MinStack()
stack.push(3)
stack.push(2)
stack.push(4)
stack.push(1)
print(stack.Top())
print(stack.getMin())
print(stack.Size())
stack.pop()
print(stack.Top())
print(stack.getMin())
print(stack.Size())

# Time Complexity: O(1)
# Space Complexity: O(n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, x):
        if x <= self.min:
            self.stack.append(2 * x - self.min)
            self.min = x
        else:
            self.stack.append(x)

    def pop(self):
        if not self.isEmpty():
            if self.stack[-1] < self.min:
                self.min = 2 * self.min - self.stack[-1]
            self.stack.pop()
        else:
            print("Stack is Empty")

    def Top(self):
        if not self.isEmpty():
            if self.stack[-1] < self.min:
                return self.min
            return self.stack[-1]
        else:
            return -1
        
    def getMin(self):
        if not self.isEmpty():
            return self.min
        else:
            return -1
        
    def Size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return not self.stack
    
    def printStack(self):
        for i in range(len(self.stack)):
            print(self.stack[i], end=" ")
        print()

print()
print("Less Space Complexity")
stack = MinStack()
stack.push(3)
stack.push(2)
stack.push(4)
stack.push(1)
print(stack.Top())
print(stack.getMin())
print(stack.Size())
stack.pop()
print(stack.Top())
print(stack.getMin())
print(stack.Size())
