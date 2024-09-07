# Set/Unset rightmost unset bit
def setUnsetBit(n):
    return n | (n + 1)

print(setUnsetBit(5))
print(setUnsetBit(6))
print(setUnsetBit(7))
print(setUnsetBit(15))
