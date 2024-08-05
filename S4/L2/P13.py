# Median of two sorted arrays
def median_two_sorted_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 > n2:
        return median_two_sorted_arrays(arr2, arr1)
    
    lo = 0
    hi = n1

    n = n1 + n2
    left = (n1 + n2 + 1)//2
    while lo <= hi:
        mid1 = (lo + hi)//2
        mid2 = left - mid1
        l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
        if mid1 < n1:
            r1 = arr1[mid1]
        if mid2 < n2:
            r2 = arr2[mid2]
        if mid1 - 1 >= 0:
            l1 = arr1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = arr2[mid2 - 1]
        
        if l1 <= r2 and l2 <= r1:
            if n % 2 == 0:
                return (max(l1, l2) + min(r1, r2))/2.0
            else:
                return max(l1, l2)
        elif l1 > r2:
            hi = mid1 - 1
        else:
            lo = mid1 + 1
    return -1

arr1 = [1, 3]
arr2 = [2]
print(median_two_sorted_arrays(arr1, arr2))
