# Minimum in Rotated Sorted Array
import sys
def minimum_in_rotated_sorted_array(array):
    low = 0
    high = len(array) - 1
    ans = sys.maxsize
    while low <= high:
        mid = (low + high)//2
        if array[low] <= array[high]:
            ans = min(ans, array[low])
            break
        if array[low] <= array[mid]:
            ans = min(ans, array[low])
            low = mid + 1
        else:
            ans = min(ans, array[mid])
            high = mid - 1
    return ans

array = [4, 5, 6, 7, 0, 1, 2]
print(minimum_in_rotated_sorted_array(array))
