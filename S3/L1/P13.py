# Longest subarray with given sum K
def longest_subarray_with_sum_k(array, k):
    left = right = 0
    current_sum = array[0]
    max_length = 0
    while right < len(array):
        while left <= right and current_sum > k:
            current_sum -= array[left]
            left += 1
        if current_sum == k:
            max_length = max(max_length, right - left + 1)
        right += 1
        if right < len(array):
            current_sum += array[right]
    return max_length

array = [4, 1, 1, 1, 2, 3, 5]
k = 5
print(longest_subarray_with_sum_k(array, k))
