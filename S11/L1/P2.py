# Min Heap and Max Heap Implementation
class MinHeap:
    def __init__(self):
        self.heap = []
    def insertKey(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i != 0 and self.heap[(i-1)//2] > self.heap[i]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1)//2
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[(i-1)//2] > self.heap[i]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1)//2
    def extractMin(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.minHeapify(0)
        return root
    def deleteKey(self, i):
        self.decreaseKey(i, float('-inf'))
        self.extractMin()
    def minHeapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest)
    def getMin(self):
        return self.heap[0]
    
class MaxHeap:
    def __init__(self):
        self.heap = []
    def insertKey(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i != 0 and self.heap[(i-1)//2] < self.heap[i]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1)//2
    def increaseKey(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[(i-1)//2] < self.heap[i]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1)//2
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
        l = 2*i + 1
        r = 2*i + 2
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
    
minHeap = MinHeap()
minHeap.insertKey(3)
minHeap.insertKey(2)
minHeap.deleteKey(1)
minHeap.insertKey(15)
minHeap.insertKey(5)
minHeap.insertKey(4)
minHeap.insertKey(45)
print(minHeap.extractMin())
print(minHeap.getMin())
minHeap.decreaseKey(2, 1)
print(minHeap.getMin())

maxHeap = MaxHeap()
maxHeap.insertKey(3)
maxHeap.insertKey(2)
maxHeap.deleteKey(1)
maxHeap.insertKey(15)
maxHeap.insertKey(5)
maxHeap.insertKey(4)
maxHeap.insertKey(45)
print(maxHeap.extractMax())
print(maxHeap.getMax())
maxHeap.increaseKey(2, 1)
print(maxHeap.getMax())
