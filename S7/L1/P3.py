# Count Good Numbers
def countGoodNumbers(n):
    MOD = 10**9 + 7
    def power(x, n):
        if n == 0:
            return 1
        answer = power(x, n // 2)
        if n % 2:
            return answer * answer * x % MOD
        else:
            return x * answer * answer % MOD
        
    return power(5, (n + 1) // 2) * power(4, n // 2) % MOD

print(countGoodNumbers(1))
print(countGoodNumbers(4))
print(countGoodNumbers(50))
print(countGoodNumbers(100))
