# Find the number that appears odd number of times
def oddNumberTimes(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

print(oddNumberTimes([1, 2, 3, 2, 3, 1, 3]))
print(oddNumberTimes([5, 7, 2, 7, 5, 2, 5]))
