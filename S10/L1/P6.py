# Count number of nice subarrays
def atMost(arr, k):
    subArrays = 0
    windowSize = 0
    start = 0
    for num in arr:
        if num % 2 == 1:
            windowSize += 1
        while windowSize > k:
            if arr[start] % 2 == 1:
                windowSize -= 1
            start += 1
        subArrays += num - start + 1
    return subArrays

def numberOfNiceSubarrays(arr, k):
    return atMost(arr, k) - atMost(arr, k - 1)

print(numberOfNiceSubarrays([1,1,2,1,1], 3))
print(numberOfNiceSubarrays([2,4,6], 1))
print(numberOfNiceSubarrays([2,2,2,1,2,2,1,2,2,2], 2))
