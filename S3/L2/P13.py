# Traverse the matrix in spiral order
def spiral_traverse_matrix(array):
    n = len(array)
    m = len(array[0])

    top = 0
    bottom = n - 1
    left = 0
    right = m - 1

    ans = []

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            ans.append(array[top][i])
        top += 1
    
        for i in range(top, bottom+1):
            ans.append(array[i][right])
        right -= 1
    
        if top <= bottom:
            for i in range(right, left-1, -1):
                ans.append(array[bottom][i])
            bottom -= 1
    
        if left <= right:
            for i in range(bottom, top-1, -1):
                ans.append(array[i][left])
            left += 1

    return ans

array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiral_traverse_matrix(array))
