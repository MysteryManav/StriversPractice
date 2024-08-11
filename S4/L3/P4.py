# Find Peak Element-II
def max_row(array, mid):
    max_val = 0
    max_index = 0
    for i in range(len(array)):
        if array[i][mid] > max_val:
            max_val = array[i][mid]
            max_index = i
    return max_index

def peak_elements(array):
    n = len(array)
    m = len(array[0])
    lo = 0
    hi = m - 1
    
    while lo <= hi:
        mid = (lo + hi)//2
        max_row_val = max_row(array, mid)
        left = array[max_row_val][mid - 1] if mid >= 0 else -1
        right = array[max_row_val][mid + 1] if mid < m - 1 else -1
        if array[max_row_val][mid] >= left and array[max_row_val][mid] >= right:
            return (max_row_val, mid)
        elif left > array[max_row_val][mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return (-1, -1)

array = [
    [10, 8, 10, 10],
    [14, 13, 12, 11],
    [15, 9, 11, 21],
    [16, 17, 19, 20]
]
print(peak_elements(array))
