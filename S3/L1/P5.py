# Left Rotate Array by One
def left_rotate_array_by_one(array):
    temp = array[0]
    for i in range(len(array) - 1):
        array[i] = array[i + 1]
    array[len(array) - 1] = temp
    return array

array = [1, 2, 3, 4, 5]
print(left_rotate_array_by_one(array))
