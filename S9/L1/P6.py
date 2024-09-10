# Implement Queue using Linked List
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.isEmpty():
            self.head = self.head.next
        else:
            print("Queue is Empty")

    def Front(self):
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
    
    def printQueue(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

queue = Queue()
queue.enqueue(6)
queue.enqueue(3)
queue.enqueue(7)
print(queue.Front())
print(queue.Size())
queue.dequeue()
print(queue.Front())
print(queue.Size())
