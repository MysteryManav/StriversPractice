# Set Matrix Zero: If an element is zero, set the entire row and colums as zero
def set_matrix_zero(array):
    n = len(array)
    m = len(array[0])
    row_zero = [False]*n
    col_zero = [False]*m

    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                row_zero[i] = True
                col_zero[j] = True

    for i in range(n):
        for j in range(m):
            if row_zero[i] or col_zero[j]:
                array[i][j] = 0

    return array

array = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
print(set_matrix_zero(array))
