# Print 1 to N
def one_to_n(n):
    if n == 10:
        print('10')
        return
    else:
        print(n)
        return one_to_n(n+1)

# Print  N to 1
def n_to_one(n):
    if n == 1:
        print("1")
        return
    else:
        print(n)
        return n_to_one(n-1)

# Sum of first N numbers
def sum_of_n_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_n_numbers(n-1)

# Factorial of N
def factorial_n(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial_n(n-1)

# Reverse an Array
def reverse_array(array, n):
    rev_array = [0]*n
    for i in range(n-1, -1, -1):
        rev_array[n-i-1] = array[i]
    return rev_array

# Check if string is palindrome or not
def palindrome_check(message):
    message_length = len(message)
    palindrome = True
    for i in range(int(message_length/2)+1):
        if message[i] != message[message_length - i - 1]:
            palindrome = False
            return palindrome
    return palindrome

# Fibonacci Number
def fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

# one_to_n(1)
# n_to_one(10)
# print(sum_of_n_numbers(7))
# print(factorial_n(5))
# print(reverse_array([1, 2, 3, 4, 5], 5))
# print(palindrome_check('malayalam'))
print(fibonacci_number(8))
