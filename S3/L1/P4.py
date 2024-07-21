# Remove Duplicates from Sorted Array
def remove_duplicates_from_sorted_array(array):
    if len(array) == 0:
        return 0
    i = 0
    for j in range(1, len(array)):
        if array[i] != array[j]:
            i += 1
            array[i] = array[j]
    return i+1

array = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
for i in range(remove_duplicates_from_sorted_array(array)):
    print(array[i], end=" ")
