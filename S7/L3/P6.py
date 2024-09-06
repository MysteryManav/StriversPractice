# M-Coloring Problem
def isSafe(v, graph, color, c, n):
    for i in range(n):
        if i != v and graph[i][v] == 1 and color[i] == c:
            return False
    return True

def solve(v, graph, m, n, color):
    if v == n:
        return True
    for c in range(1, m + 1):
        if isSafe(v, graph, color, c, n):
            color[v] = c
            if solve(v + 1, graph, m, n, color):
                return True
            color[v] = 0
    return False

def mColoring(graph, m, n):
    color = [0] * n
    if solve(0, graph, m, n, color):
        return True
    return False

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3
n = 4
print(mColoring(graph, m, n))
