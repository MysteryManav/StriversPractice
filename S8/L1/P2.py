# Check if i-th bit is set or not
def checkBitSet(num, i):
    if num & (1 << i):
        return True
    return False

print(checkBitSet(5, 0))
print(checkBitSet(5, 1))
print(checkBitSet(5, 2))
print(checkBitSet(5, 3))
