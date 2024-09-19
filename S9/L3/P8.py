# Sum of subarray ranges
def sumOfSubarrayMinimums(arr):
    n = len(arr)
    left = [None] * n
    right = [None] * n
    s1 = []
    s2 = []
    for i in range(n):
        count = 1
        while s1 and s1[-1][0] >= arr[i]:
            count += s1.pop()[1]
        left[i] = count
        s1.append((arr[i], count))
    for i in range(n-1, -1, -1):
        count = 1
        while s2 and s2[-1][0] > arr[i]:
            count += s2.pop()[1]
        right[i] = count
        s2.append((arr[i], count))
    res = 0
    for i in range(n):
        res += arr[i] * left[i] * right[i]
    return res

def sumOfSubarrayMaximums(arr):
    n = len(arr)
    left = [None] * n
    right = [None] * n
    s1 = []
    s2 = []
    for i in range(n):
        count = 1
        while s1 and s1[-1][0] <= arr[i]:
            count += s1.pop()[1]
        left[i] = count
        s1.append((arr[i], count))
    for i in range(n-1, -1, -1):
        count = 1
        while s2 and s2[-1][0] < arr[i]:
            count += s2.pop()[1]
        right[i] = count
        s2.append((arr[i], count))
    res = 0
    for i in range(n):
        res += arr[i] * left[i] * right[i]
    return res

def sumOfSubarrayRanges(arr):
    min_vals = sumOfSubarrayMinimums(arr)
    max_vals = sumOfSubarrayMaximums(arr)
    return (max_vals - min_vals)

print(sumOfSubarrayRanges([1, 2, 3]))
print(sumOfSubarrayRanges([1, 3, 3]))
print(sumOfSubarrayRanges([4, -2, -3, 4, 1]))
