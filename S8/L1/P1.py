# Bit Manipulation
def getBit(num, n):
    return (num >> n) & 1

def setBit(num, n):
    return num | (1 << (n - 1))

def clearBit(num, n):
    return ~(1 << (n - 1)) & num

num = 5
n = 1
print(getBit(num, n))
print(setBit(num, n))
print(clearBit(num, n))
