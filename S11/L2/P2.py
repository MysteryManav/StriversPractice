# Kth largest/smallest element in an array
def parent(i):
    return (i - 1)//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(arr, i, heap_size):
    l = left(i)
    r = right(i)
    largest = i
    if l < heap_size and arr[l] > arr[i]:
        largest = l
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)

def build_max_heap(arr):
    heap_size = len(arr)
    for i in range(len(arr)//2, -1, -1):
        max_heapify(arr, i, heap_size)

def heap_sort(arr):
    build_max_heap(arr)
    heap_size = len(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0, heap_size)

def kth_element(arr, k):
    heap_sort(arr)
    print("Kth largest element: ", arr[-k])
    print("Kth smallest element: ", arr[k-1])

kth_element([3, 2, 1, 5, 6, 4], 2)
kth_element([12, 3, 5, 7, 19], 4)
kth_element([1, 2, 3, 4, 5, 6, 7], 3)
