# Search Single Element in Sorted Array
def single_element_in_sorted_array(array):
    n = len(array)

    if n == 0:
        return array[0]
    elif array[0] != array[1]:
        return array[0]
    elif array[n - 1] != array[n - 2]:
        return array[n - 1]
    
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high)//2
        if array[mid] != array[mid - 1] and array[mid] != array[mid + 1]:
            return array[mid]
        if (mid % 2 == 0 and array[mid] == array[mid + 1]) or (mid % 2 == 1 and array[mid] == array[mid - 1]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7]
print(single_element_in_sorted_array(array))
