# Sliding Window Maximum
def slidingWindowMaximum(nums, k):
    if k == 1:
        return nums

    n = len(nums)
    result = []
    suffix = [0] * k
    
    for i in range(k, n + 1, k):
        suffix[0] = nums[i - 1] 
        for j in range(1, k):
            suffix[j] = max(suffix[j - 1], nums[i - j - 1])
        cmax = -float("inf")
        for idx in range(k):
            result.append(max(cmax, suffix[k - idx - 1]))
            if i + idx >= n: break
            cmax = max(cmax, nums[i + idx])
    
    return result

print(slidingWindowMaximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(slidingWindowMaximum([1, 3, -1, -3, 5, 3, 6, 7], 1))
print(slidingWindowMaximum([4,0,-1,3,5,3,6,8], 3))
print(slidingWindowMaximum([1,3,1,2,0,5], 3))
