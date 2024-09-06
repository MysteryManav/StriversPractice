# N-Queen Problem
def solve(row, n, board, answer, leftrow, upperdiag, lowerdiag,):
    if row == n:
        temp = []
        for i in range(n):
            temp.append(''.join(board[i]))
        answer.append(temp)
        return
    for col in range(n):
        if leftrow[col] or upperdiag[row + col] or lowerdiag[row - col + n - 1]:
            continue
        leftrow[col] = upperdiag[row + col] = lowerdiag[row - col + n - 1] = 1
        board[row][col] = 'Q'
        solve(row + 1, n, board, answer, leftrow, upperdiag, lowerdiag)
        leftrow[col] = upperdiag[row + col] = lowerdiag[row - col + n - 1] = 0
        board[row][col] = '.'
    return

def solveNQueens(n):
    answer = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    leftrow = [0] * n
    upperdiag = [0] * (2 * n - 1)
    lowerdiag = [0] * (2 * n - 1)
    solve(0, n, board, answer, leftrow, upperdiag, lowerdiag,)
    if answer:
        printSolution(answer)
    else:
        print("No Solution")

def printSolution(answer):
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            print(answer[i][j])
        print()
    print(f"Found {len(answer)} solutions")

n = 8
solveNQueens(n)
