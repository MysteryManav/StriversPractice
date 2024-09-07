# Find two numbers appearing odd number of times
def twoNumberOddTimes(nums):
    xor = 0
    for num in nums:
        xor ^= num
    rightmost_set_bit = xor & -xor
    num1 = 0
    num2 = 0
    for num in nums:
        if num & rightmost_set_bit:
            num1 ^= num
        else:
            num2 ^= num
    return num1, num2

print(twoNumberOddTimes([4, 2, 4, 5, 2, 3, 3, 1]))
print(twoNumberOddTimes([1, 2, 3, 2, 1, 4, 5, 4]))
print(twoNumberOddTimes([1, 2, 3, 2, 1, 4, 5, 4, 5, 6]))
