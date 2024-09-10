# Print Prime Factors of a number
def primeFactorsOfNumber(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            print(i, end=' ')
    if n > 1:
        print(n)

primeFactorsOfNumber(780)
primeFactorsOfNumber(60)
primeFactorsOfNumber(35)
