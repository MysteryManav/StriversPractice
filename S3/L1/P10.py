# Find missing number in an array
def missing_number_in_array(array, n):
    expected = n * (n+1) // 2
    actual = sum(array)
    return expected - actual

def missing_number_in_array_xor(array, n):
    xor_1 = 0
    xor_2 = 0
    for i in range(0, n+1):
        xor_1 ^= i
    for i in array:
        xor_2 ^= i

    return xor_1 ^ xor_2

array = [1, 2, 3, 4, 5, 6, 8, 9, 10]
n = 10
print(missing_number_in_array(array, n))
print(missing_number_in_array_xor(array, n))
