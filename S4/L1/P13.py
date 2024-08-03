# Find Peak Element
def peak_element(array):
    n = len(array)
    
    if n == 1:
        return array[0]
    elif array[0] > array[1]:
        return array[0]
    elif array[n - 1] > array[n - 2]:
        return array[n - 1]
    
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high)//2
        if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
            return array[mid]
        if array[mid] > array[mid - 1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [1, 2, 1, 3, 4, 2, 5, 6, 7, 8, 9, 10, 11, 12, 1]
print(peak_element(array))
