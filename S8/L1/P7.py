# Swap Two Numbers using bit manipulation
def swapTwoNumbers(n1, n2):
    n1 = n1 ^ n2
    n2 = n1 ^ n2
    n1 = n1 ^ n2
    return n1, n2

print(swapTwoNumbers(5, 6))
print(swapTwoNumbers(7, 8))
print(swapTwoNumbers(9, 10))
