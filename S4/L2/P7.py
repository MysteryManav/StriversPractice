# K-th Missing Number in a strictly increasing array
def kth_misssing_number(array, k):
    n=len(array)
    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = (lo + hi)//2
        missing = array[mid] - mid + 1
        if missing < k:
            lo = mid + 1
        else:
            hi = mid - 1
    return k + lo + 1

array = [2, 3, 4, 7, 11]
k = 5
print(kth_misssing_number(array, k))
