# Rat in a Maze Problem
def solveMaze(maze, row, col, n, visited, answer, move):
    if row == n - 1 and col == n - 1:
        answer.append(move)
        return
    
    # Downward
    if row + 1 < n and maze[row + 1][col] == 1 and not visited[row + 1][col]:
        visited[row + 1][col] = 1
        solveMaze(maze, row + 1, col, n, visited, answer, move+'D')
        visited[row + 1][col] = 0
    
    # Upward
    if row - 1 >= 0 and maze[row - 1][col] == 1 and not visited[row - 1][col]:
        visited[row - 1][col] = 1
        solveMaze(maze, row - 1, col, n, visited, answer, move+'U')
        visited[row - 1][col] = 0
    
    # Rightward
    if col + 1 < n and maze[row][col + 1] == 1 and not visited[row][col + 1]:
        visited[row][col + 1] = 1
        solveMaze(maze, row, col + 1, n, visited, answer, move+'R')
        visited[row][col + 1] = 0
    
    # Leftward
    if col - 1 >= 0 and maze[row][col - 1] == 1 and not visited[row][col - 1]:
        visited[row][col - 1] = 1
        solveMaze(maze, row, col - 1, n, visited, answer, move+'L')
        visited[row][col - 1] = 0

def printSolution(answer):
    for i in range(len(answer)):
        print(answer[i])
    print(f"Found {len(answer)} solutions")

def findPath(maze, n):
    answer = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    solveMaze(maze, 0, 0, n, visited, answer, '')
    if answer:
        printSolution(answer)
    else:
        print("No Solution")

n = 8
maze = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
findPath(maze, n)
