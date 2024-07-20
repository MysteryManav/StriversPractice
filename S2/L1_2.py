# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr
    for i in range(n-1, 0, -1):
        for j in range(i):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    return sorted_arr

print(bubble_sort([3, 4, 2, 1, 5, 0]))
