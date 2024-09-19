# Next Smaller Element
def nextSmallestElement(arr):
    n = len(arr)
    stack = []
    res = [-1] * n
    for i in range(2*n-1, -1, -1):
        while stack and stack[-1] >= arr[i%n]:
            stack.pop()
        if i < n:
            if stack:
                res[i] = stack[-1]
        stack.append(arr[i%n])
    return res

print(nextSmallestElement([4, 5, 2, 10, 8]))
print(nextSmallestElement([3, 2, 1]))
