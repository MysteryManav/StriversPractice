# Implement Queue using Arrays
class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.size = 1000
        self.queue = [0]*self.size

    def enqueue(self, x):
        if not self.isFull():
            self.queue[self.rear] = x
            self.rear += 1
        else:
            print("Queue is Full")
    
    def dequeue(self):
        if not self.isEmpty():
            self.front += 1
        else:
            print("Queue is Empty")

    def Front(self):
        if not self.isEmpty():
            return self.queue[self.front]
        else:
            return -1
        
    def Size(self):
        return self.rear - self.front
    
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.rear == self.size
    
    def printQueue(self):
        for i in range(self.front, self.rear):
            print(self.queue[i], end=" ")
        print()

queue = Queue()
queue.enqueue(6)
queue.enqueue(3)
queue.enqueue(7)
print(queue.Front())
print(queue.Size())
queue.dequeue()
print(queue.Size())
print(queue.Front())
queue.printQueue()
