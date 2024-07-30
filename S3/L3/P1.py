# Pascal's Triangle
def pascal_variation_one(row, column):
    res = 1
    for i in range(column):
        res = res * (row - i)
        res = res // (i + 1)
    return res

def pascal_variation_two(row):
    ans = [1]*row
    for i in range(1, row):
        ans[i] = ans[i-1] * (row - i)
        ans[i] = ans[i] // i
    print(ans)

def pascal_variation_three(row):
    ans = 1
    ans_row = [1]

    for i in range(1, row):
        ans = ans * (row - i)
        ans = ans // i
        ans_row.append(ans)
    return ans_row

def pascal_triangle(row, column):
    print(pascal_variation_one(row - 1, column - 1))
    pascal_variation_two(row)
    for i in range(row+1):
        print(pascal_variation_three(i))

row = 10
column = 7
pascal_triangle(row, column)
