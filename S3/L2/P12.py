# Rotate matrix by 90 degrees
def rotate_90(array):
    n = len(array)

    for i in range(n):
        for j in range(i):
            array[i][j], array[j][i] = array[j][i], array[i][j]

    for i in range(n):
        array[i].reverse()

    return array

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_90(array))
