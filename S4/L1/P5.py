# Floor and Ceil in Sorted Array
def floor_ceil_sorted_array(array, target):
    low = 0
    high = len(array) - 1
    floor_value = -1
    ceil_value = -1
    while low <= high:
        mid = (low + high)//2
        if array[mid] <= target:
            floor_value = array[mid]
            low = mid + 1
        else:
            ceil_value = array[mid]
            high = mid - 1

    return floor_value, ceil_value

array = [1, 2, 8, 10, 10, 12, 19]
target = 5
print(floor_ceil_sorted_array(array, target))
