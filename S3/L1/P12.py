# Find the number that appears only once, when all other numbers appear twice
def single_number(array):
    result = 0
    for i in range(len(array)):
        result ^= array[i]
    return result

array = [1, 2, 3, 4, 1, 2, 4]
print(single_number(array))
