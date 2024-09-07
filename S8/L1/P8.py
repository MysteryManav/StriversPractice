# Divide two integers without multiplication, division and mod operators
def divideTwoIntegers(n1, n2):
    sign = True
    if n1 >= 0 and n2 < 0 or n1 < 0 and n2 >= 0:
        sign = False

    n1 = abs(n1)
    n2 = abs(n2)
    result = 0
    while n1 >= n2:
        count = 0
        while n1 >= (n2 << (count+1)):
            count += 1
        result += 1 << count
        n1 -= n2 << count
    if not sign:
        result = -result
    return result

print(divideTwoIntegers(10, 3))
print(divideTwoIntegers(7, -3))
print(divideTwoIntegers(-7, 3))
print(divideTwoIntegers(-7, -3))
print(divideTwoIntegers(0, 3))
print(divideTwoIntegers(7, 1))
