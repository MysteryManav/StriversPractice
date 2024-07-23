# Longest Consecutive Sequence in an Array
def longest_consecutive_sequence(array):
    n = len(array)
    array_set = set(array)
    max_length = 0

    for element in array_set:
        if element-1 not in array_set:
            current_element = element
            current_length = 1

        while current_element+1 in array_set:
            current_element += 1
            current_length += 1

        max_length = max(max_length, current_length)

    return max_length

array = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(array))
