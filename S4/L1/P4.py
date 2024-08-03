# Search Insert Position
def search_insert_position(array, target):
    low = 0
    high = len(array) - 1
    result = len(array)
    while low <= high:
        mid = (low + high)//2
        if array[mid] >= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

array = [1, 3, 5, 6]
target = 4
print(search_insert_position(array, target))
