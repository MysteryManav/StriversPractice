# Binary Search Implementation
def binary_search(array, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high)//2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, mid+1, high, target)
    else:
        return binary_search(array, low, mid-1, target)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
print(binary_search(a, 0, len(a)-1, target))
