# Selection Sort Algorithm
def selection_sort(arr):
    n = len(arr)
    sorted_arr = arr
    for i in range(0, n-1):
        min = sorted_arr[i]
        for j in range(i, n):
            if sorted_arr[j] < min:
                min = j
        sorted_arr[i], sorted_arr[min] = sorted_arr[min], sorted_arr[i]
    return sorted_arr

print(selection_sort([3, 4, 2, 1, 5, 0]))
