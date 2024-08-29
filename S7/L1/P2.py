# Calculate x raised to power n
def power(x, n):
    if n == 0:
        return 1
    answer = power(x, n // 2)
    if n % 2:
        return answer * answer * x
    else:
        return x * answer * answer

print(power(2.0, 3))
print(power(3, 3))
print(power(2.1, 3))
