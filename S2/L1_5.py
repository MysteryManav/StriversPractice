# Quick Sort
def partition(array, low, high):
    pivot = array[low]
    i = low
    j = high
    while i < j:
        while array[i] <= pivot and i < high:
            i += 1
        while array[j] > pivot and j > low:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
    array[low], array[j] = array[j], array[low]
    return j

def quick_sort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)
        quick_sort(array, low, partition_index-1)
        quick_sort(array, partition_index+1, high)

array = [3, 4, 2, 1, 5, 0]
quick_sort(array, 0, len(array)-1)
print(array)
