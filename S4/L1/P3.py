# Implement Upper Bound
def upper_bound(array, target):
    low = 0
    high = len(array) - 1
    upper_bound = len(array)

    while low <= high:
        mid = (low + high) // 2
        if array[mid] > target:
            upper_bound = mid
            high = mid - 1
        else:
            low = mid + 1
    return upper_bound

array = [3, 5, 8, 9, 15, 19]
target = 9
print(upper_bound(array, target))
