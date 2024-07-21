# Longest Subarray with sum k (positive and negative numbers)
def longest_subarray_with_sum_k(array, k):
    n = len(array)
    prefix_sum = {}
    current_sum = 0
    max_length = 0

    for i in range(n):
        current_sum += array[i]
        if current_sum == k:
            max_length = max(max_length, i + 1)
        remaining = current_sum - k
        if remaining in prefix_sum:
            max_length = max(max_length, i - prefix_sum[remaining])
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    return max_length

array = [4, 1, 1, 1, 2, 3, 5]
k = 5
print(longest_subarray_with_sum_k(array, k))
