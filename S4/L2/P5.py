# Find the smallest divisor given a threshold
import math

def divisor_sum(nums, divisor):
    total_sum = 0
    for num in nums:
        total_sum += math.ceil(num/divisor)
    return total_sum

def smallest_divisor(nums, threshold):
    n = len(nums)
    if n > threshold:
        return -1
    lo = 1
    hi = max(nums)

    while lo <= hi:
        mid = (lo + hi)//2
        if divisor_sum(nums, mid) <= threshold:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

print(smallest_divisor([1, 2, 5, 9], 6))
print(smallest_divisor([1, 2, 3, 4, 5], 8))
