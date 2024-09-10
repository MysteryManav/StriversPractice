# Power(n, x)
def power(n, x):
    ans = 1
    while x > 0:
        if x % 2 == 1:
            ans = ans * n
            x = x - 1
        else:
            x = x/2
            n = n * n
    return ans

print(power(2, 3))
print(power(2, 4))
print(power(2, 8))
print(power(3, 4))
print(power(5, 5))
print(power(7, 6))
print(power(11, 7))
print(power(13, 8))
print(power(17, 9))
print(power(19, 10))
