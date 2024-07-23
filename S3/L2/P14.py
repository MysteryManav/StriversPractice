# Count subarrays with sum K
from collections import defaultdict

def count_subarrays_sum_k(array, k):
    n = len(array)
    prefix_sum = 0
    count = 0
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1

    for i in range(n):
        prefix_sum += array[i]
        count += prefix_sum_count[prefix_sum - k]
        prefix_sum_count[prefix_sum] += 1

    return count

array = [3, 1, 2, 4]
k = 6
print(count_subarrays_sum_k(array, k))
