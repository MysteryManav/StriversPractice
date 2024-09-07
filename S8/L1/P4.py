# Check if a number is power of two or not
def checkPowerOfTwo(num):
    if num & (num - 1):
        return False
    return True

print(checkPowerOfTwo(1))
print(checkPowerOfTwo(2))
print(checkPowerOfTwo(3))
print(checkPowerOfTwo(4))
print(checkPowerOfTwo(5))
print(checkPowerOfTwo(7))
print(checkPowerOfTwo(8))
