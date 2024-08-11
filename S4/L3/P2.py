# Search in a 2D Sorted Array
def search_2d_array(array, target):
    n = len(array)
    m = len(array[0])
    lo = 0
    hi = n*m - 1
    while lo <= hi:
        mid = (lo + hi)//2
        row = mid // m
        col = mid % m
        if array[row][col] == target:
            return True
        elif array[row][col] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

array = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(search_2d_array(array, target))
