# Find XOR of numbers from L to R
def xorLToR(L, R):
    N = R - L + 1
    if N % 4 == 0:
        return R
    if N % 4 == 1:
        return 1
    if N % 4 == 2:
        return R + 1
    return 0

print(xorLToR(1, 4))
print(xorLToR(2, 4))
print(xorLToR(3, 4))
print(xorLToR(1, 10))
print(xorLToR(1, 100))
