# Next Greater Element - 2 using Stack
def nextGreaterElement(arr):
    n = len(arr)
    stack = []
    res = [-1] * n
    for i in range(2*n-1, -1, -1):
        while stack and stack[-1] <= arr[i%n]:
            stack.pop()
        if i < n:
            if stack:
                res[i] = stack[-1]
        stack.append(arr[i%n])
    return res

print(nextGreaterElement([4, 5, 2, 10, 8]))
print(nextGreaterElement([3, 2, 1]))
