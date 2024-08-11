# Search in a row and column-wise sorted matrix
def search_2d_array_sorted_row_column_wise(array, target):
    n = len(array)
    m = len(array[0])
    row = 0
    col = m - 1
    while row < n and col >= 0:
        if array[row][col] == target:
            return True
        elif array[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

array = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(search_2d_array_sorted_row_column_wise(array, target))
