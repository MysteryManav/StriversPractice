# Sieve of Eratosthenes
def sieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            print(p, end=' ')
    print()

sieveOfEratosthenes(30)
sieveOfEratosthenes(100)
