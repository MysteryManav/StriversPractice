# Subarrays with K different integers
def atMost(nums, k):
    n = len(nums)
    if k == 0:
        return 0
    start = 0
    end = 0
    count = 0
    num_count = {}
    while end < n:
        num_count[nums[end]] = num_count.get(nums[end], 0) + 1
        while len(num_count) > k:
            num_count[nums[start]] -= 1
            if num_count[nums[start]] == 0:
                del num_count[nums[start]]
            start += 1
        count += end - start + 1
        end += 1
    return count

def subarraysKDistinct(nums, k):
    return atMost(nums, k) - atMost(nums, k - 1)

print(subarraysKDistinct([1,2,1,2,3], 2))
print(subarraysKDistinct([1,2,1,3,4], 3))
