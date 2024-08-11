# Find Matrix Median
def upper_bound(array, x):
    lo = 0
    hi = len(array) - 1
    ans = len(array)
    while lo <= hi:
        mid = (lo + hi)//2
        if array[mid] > x:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

def smaller_than_mid(array, mid):
    count = 0
    for i in range(len(array)):
        count += upper_bound(array[i], mid)
    return count

def find_matrix_median(array):
    n = len(array)
    m = len(array[0])
    lo = float('inf')
    hi = float('-inf')
    for i in range(n):
        lo = min(lo, array[i][0])
        hi = max(hi, array[i][m - 1])
    
    required = (n * m)//2
    while lo <= hi:
        mid = (lo + hi)//2
        count = smaller_than_mid(array, mid)
        if count <= required:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

array = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print(find_matrix_median(array))
