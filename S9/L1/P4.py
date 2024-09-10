# Implement Queue using Stack
from queue import LifoQueue

class Queue:
    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()
    
    def enqueue(self, x):
        while not self.s1.empty():
            self.s2.put(self.s1.get())
        self.s1.put(x)
        while not self.s2.empty():
            self.s1.put(self.s2.get())
    
    def dequeue(self):
        if not self.isEmpty():
            return self.s1.get()
        else:
            print("Queue is Empty")
            return -1

    def Top(self):
        if not self.isEmpty():
            return self.s1.queue[0]
        else:
            return -1
        
    def Size(self):
        return self.s1.qsize()
    
    def isEmpty(self):
        return self.s1.empty()
    
    def printQueue(self):
        for i in range(self.s1.qsize()):
            print(self.s1.queue[i], end=" ")
        print()

queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
queue.enqueue(5)
print(queue.Top())
print(queue.Size())
