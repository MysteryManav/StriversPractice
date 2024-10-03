# Convert Min Heap to Max Heap
def parent(i):
    return (i - 1)//2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(arr, i):
    n = len(arr)
    l = left(i)
    r = right(i)
    largest = i
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)

def min_heap_to_max_heap(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        max_heapify(arr, i)
    return arr

print(min_heap_to_max_heap([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]))
print(min_heap_to_max_heap([1, 2, 3, 4]))
print(min_heap_to_max_heap([3, 4, 8, 11, 13]))
