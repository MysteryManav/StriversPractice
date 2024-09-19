# Sum of subarray minimum
def sumOfSubarrayMinimums(arr):
    n = len(arr)
    left = [None] * n
    right = [None] * n
    s1 = []
    s2 = []
    for i in range(n):
        count = 1
        while s1 and s1[-1][0] > arr[i]:
            count += s1.pop()[1]
        left[i] = count
        s1.append((arr[i], count))
    for i in range(n-1, -1, -1):
        count = 1
        while s2 and s2[-1][0] >= arr[i]:
            count += s2.pop()[1]
        right[i] = count
        s2.append((arr[i], count))
    res = 0
    for i in range(n):
        res += arr[i] * left[i] * right[i]
    return res % (10**9 + 7)

print(sumOfSubarrayMinimums([3, 1, 2, 4]))
print(sumOfSubarrayMinimums([11, 81, 94, 43, 3]))
