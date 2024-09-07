# Find the total count of set bits for all numbers from 1 to n
def countSetBitsUtil(i):
    if i <= 0:
        return 0
    return (0 if i & 1 == 0 else 1) + countSetBitsUtil(i >> 1)

def countSetBits(n):
    count = 0
    for i in range(1, n):
        count += countSetBitsUtil(i)
    return count

print(countSetBits(5))
print(countSetBits(6))
