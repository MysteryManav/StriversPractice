# K-th element of two sorted arrays
def kth_element_two_sorted_arrays(arr1, arr2, k):
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 > n2:
        return kth_element_two_sorted_arrays(arr2, arr1, k)
    
    left = k
    lo = max(0, k - n2)
    hi = min(k, n1)
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
            return max(l1, l2)
        elif l1 > r2:
            hi = mid1 - 1
        else:
            lo = mid1 + 1
    return -1

arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
k = 3
print(kth_element_two_sorted_arrays(arr1, arr2, k))
