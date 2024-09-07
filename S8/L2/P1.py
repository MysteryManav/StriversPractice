# Count number of bits to be flipped to convert A to B
def countBitsFlip(a, b):
    count = a ^ b
    result = 0
    while count:
        if count & 1:
            result += 1
        count >>= 1
    return result

print(countBitsFlip(10, 20))
print(countBitsFlip(10, 7))
print(countBitsFlip(3, 4))
