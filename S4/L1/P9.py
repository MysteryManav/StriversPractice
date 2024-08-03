# Search Element in a Rotated Sorted Array
def element_in_rotated_sorted_array_2(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high)//2
        if array[mid] == target:
            return True
        
        if array[low] == array[mid] and array[mid] == array[high]:
            low += 1
            high -= 1
            continue

        if array[low] <= array[mid]:
            if array[low] <= target <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if array[mid] <= target <= array[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False

array = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(element_in_rotated_sorted_array_2(array, target))
