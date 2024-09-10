# All divisors of a number
def divisorsOfNumber(n):
    i = 1
    while i*i <= n:
        if n%i == 0:
            if i == n//i:
                print(i, end = " ")
            else:
                print(i, n//i, end = " ")
        i += 1
    print()
    return

divisorsOfNumber(100)
divisorsOfNumber(10)
