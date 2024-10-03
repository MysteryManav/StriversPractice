# Implementation of Priority Queue using Binary Heap
def parent(i):
    return (i-1)//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

class MaxHeapPriorityQueue:
    def __init__(self):
        self.heap = []
    def insertKey(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i != 0 and self.heap[parent(i)] < self.heap[i]:
            self.heap[parent(i)], self.heap[i] = self.heap[i], self.heap[parent(i)]
            i = parent(i)
    def increaseKey(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[parent(i)] < self.heap[i]:
            self.heap[parent(i)], self.heap[i] = self.heap[i], self.heap[parent(i)]
            i = parent(i)
    def extractMax(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.maxHeapify(0)
        return root
    def deleteKey(self, i):
        self.increaseKey(i, float('inf'))
        self.extractMax()
    def maxHeapify(self, i):
        l = left(i)
        r = right(i)
        largest = i
        if l < len(self.heap) and self.heap[l] > self.heap[i]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)
    def getMax(self):
        return self.heap[0]

maxHeap = MaxHeapPriorityQueue()
maxHeap.insertKey(4)
maxHeap.insertKey(2)
maxHeap.insertKey(8)
maxHeap.insertKey(16)
maxHeap.insertKey(24)
maxHeap.insertKey(2)
maxHeap.insertKey(6)
maxHeap.insertKey(5)
print(maxHeap.extractMax())
print(maxHeap.getMax())
print(maxHeap.heap)
