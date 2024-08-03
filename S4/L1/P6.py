# Last Occurence in a Sorted Array
def last_occurence_sorted_array(array, target):
    low = 0
    high = len(array) - 1
    result = -1
    while low <= high:
        mid = (low + high)//2
        if array[mid] == target:
            result = mid
            low = mid + 1
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

array = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
target = 2
print(last_occurence_sorted_array(array, target))
