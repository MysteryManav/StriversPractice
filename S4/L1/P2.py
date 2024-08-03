# Lower Bound
def lower_bound(array, target):
    low = 0
    high = len(array) - 1
    low_bound = len(array)
    while low <= high:
        mid = (low + high)//2
        if array[mid] >= target:
            low_bound = mid
            high = mid - 1
        else:
            low = mid + 1
    return low_bound

array = [3, 5, 8, 15, 19]
target = 9
print(lower_bound(array, target))
