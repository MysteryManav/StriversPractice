# Find row with maximum number of 1's
def lower_bound(array, target):
    n = len(array)
    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = (lo + hi)//2
        if array[mid] >= target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

def max_no_of_ones(array):
    n = len(array)
    lo = 0
    hi = n - 1
    max_count = 0
    max_count_index = -1
    for row in range(n):
        count_ones = len(array[row]) - lower_bound(array[row], 1)
        if count_ones > max_count:
            max_count = count_ones
            max_count_index = row
    return max_count_index

array = [[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
print(max_no_of_ones(array))
