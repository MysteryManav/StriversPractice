# Sort an array of 0s, 1s and 2s: Variation of Dutch National Flag algorithm
def sort_array(array):
    low = 0
    mid = 0
    high = len(array) - 1
    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        elif array[mid] == 2:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
        else:
            return "Invalid Input"
    return array

array = [0, 1, 2, 0, 1, 2, 0, 1, 2]
print(sort_array(array))
