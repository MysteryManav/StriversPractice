# Count Occurences in Sorted Array
def first_occurence_sorted_array(array, target):
    low = 0
    high = len(array) - 1
    result = -1
    while low <= high:
        mid = (low + high)//2
        if array[mid] == target:
            result = mid
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

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

def count_occurences_sorted_array(array, target):
    first_occurence = first_occurence_sorted_array(array, target)
    last_occurence = last_occurence_sorted_array(array, target)
    return last_occurence - first_occurence + 1

array = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
target = 2
print(count_occurences_sorted_array(array, target))
