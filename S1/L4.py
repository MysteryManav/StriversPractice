from math import log10, sqrt

number = 1234321

# Count Digits
no_of_digits = int(log10(number) + 1)
print(f"Number of digits in the given number are: {no_of_digits}")

# Reverse Number
cpy_num = number
rev_num = 0
while cpy_num > 0:
    remainder = cpy_num % 10
    rev_num = remainder + rev_num*10
    cpy_num = int(cpy_num/10)
print(f"Reversed number is: {rev_num}")

# Palindrome
if rev_num == number:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")

# GCD - Euclidean Algorithm
a = 6
b = 18
while a != 0:
    a, b = b % a, a

print(f"The GCD is: {b}")

# Armstrong Number
number = 153
k = len(str(number))
sum = 0
n = number
while n > 0:
    ld = n % 10
    sum += ld ** k
    n = n // 10

if sum == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

# Print all Divisors
# Check if number is prime or not
number = 79
num_sqrt = int(sqrt(number))

divisors = []
counter = 0

for i in range(1, num_sqrt + 1):
    if number % i == 0:
        divisors.append(i)
        counter += 1
        if i != number // i:
            counter += 1
            divisors.append(number // i)

print(f"The divisors are: {divisors}")

if counter == 2:
    print("Number is prime")
else:
    print("Number is not prime")
