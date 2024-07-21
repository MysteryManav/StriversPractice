# Check if an array is sorted
def is_sorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True

array = [12, 34, 45, 9, 8, 90, 3]
# array = [1, 2, 3, 4, 5, 6, 7]
print(is_sorted(array))
