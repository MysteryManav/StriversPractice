# The Celebrity Problem
def celebrityProblem(matrix, n):
    stack = []
    for i in range(n):
        stack.append(i)
    
    while stack:
        a = stack.pop()
        if not stack: return a
        b = stack.pop()
        if matrix[a][b]:
            stack.append(b)
        else:
            stack.append(a)
    
    return -1

matrix = [[0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0]]
n = 4
print(celebrityProblem(matrix, n))
