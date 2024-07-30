# Largest Subarray with sum 0
def largest_subarray_with_sum_0(array):
    n = len(array)
    prefix_sum = 0
    prefix_sum_map = {}
    max_length = 0

    for i in range(n):
        prefix_sum += array[i]
        
        if prefix_sum == 0:
            max_length = i + 1
        else:
            if prefix_sum in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[prefix_sum])
            else:
                prefix_sum_map[prefix_sum] = i

    return max_length

array = [15, -2, 2, -8, 1, 7, 10, 23]
print(largest_subarray_with_sum_0(array))
