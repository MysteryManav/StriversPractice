# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    sorted_arr = arr
    for i in range(1, n):
        for j in range(i, 0, -1):
            if sorted_arr[j] < sorted_arr[j-1]:
                sorted_arr[j], sorted_arr[j-1] = sorted_arr[j-1], sorted_arr[j]
    return sorted_arr

print(insertion_sort([3, 4, 2, 1, 5, 0]))
