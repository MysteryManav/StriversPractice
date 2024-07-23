# Next Permutation
def next_permutation(array):
    n = len(array)

    break_point_index = -1

    for i in range(n-2, -1, -1):
        if array[i] < array[i+1]:
            break_point_index = i
            break
    
    if break_point_index == -1:
        return array[::-1]
    
    for i in range(n-1, break_point_index, -1):
        if array[i] > array[break_point_index]:
            array[i], array[break_point_index] = array[break_point_index], array[i]
            break

    array[break_point_index+1:] = array[break_point_index+1:][::-1]

    return array

array = [3, 1, 2]
print(next_permutation(array))
