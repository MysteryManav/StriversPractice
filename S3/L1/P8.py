# Linear Search
def linear_search(array, num):
    n = len(array)
    for i in range(n):
        if array[i] == num:
            return i
    return -1

array = [12, 34, 45, 9, 8, 90, 3]
num = 90
print(linear_search(array, num))
