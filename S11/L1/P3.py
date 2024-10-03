# Check if an array is a (max) heap or not
def parent(i):
    return (i-1)//2

def is_heap(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[parent(i)] < arr[i]:
            return False
    return True

print(is_heap([90, 15, 10, 7, 12, 2]))
print(is_heap([9, 15, 10, 7, 12, 11]))
print(is_heap([90, 15, 10, 7, 12, 11]))
print(is_heap([90, 15, 10, 7, 12, 11, 6]))
