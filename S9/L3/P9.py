# Remove K Digits
def removeKDigits(num, k):
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack).lstrip('0') or '0'

print(removeKDigits('1432219', 3))
print(removeKDigits('10200', 1))
print(removeKDigits('10', 2))
