# Find how many times an array has been rotated
def number_of_times_array_rotated(array):
    low = 0
    high = len(array) - 1
    ans = float('inf')
    index = -1
    while low <= high:
        mid = (low + high)//2

        if array[low] <= array[high]:
            if array[low] < ans:
                ans = array[low]
                index = low
            break

        if array[low] <= array[mid]:
            if array[low] < ans:
                ans = array[low]
                index = low
            low = mid + 1
        else:
            if array[mid] < ans:
                ans = array[mid]
                index = mid
            high = mid - 1
    return index

array = [4, 5, 6, 7, 0, 1, 2]
print(number_of_times_array_rotated(array))
