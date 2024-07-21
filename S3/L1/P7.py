# Move all Zeros to end of array
def move_zeros_to_end(array):
    n = len(array)
    for j in range(n):
        if array[j] == 0:
            for i in range(j+1, n):
                if array[i] != 0:
                    array[i], array[j] = array[j], array[i]
                    j += 1
    return array

array = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print(move_zeros_to_end(array))
