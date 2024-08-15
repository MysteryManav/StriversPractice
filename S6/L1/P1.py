# Introduction to LinkedList
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

x = Node(2)

print(x.data)

y = x
print(y)
print(y.data)
