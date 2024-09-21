# Binary Subarray with Sum
def binarySubarrayWithSum(arr, sum):
    count = {0: 1}
    curr_sum = 0
    total_subarrays = 0
    for num in arr:
        curr_sum += num
        if curr_sum - sum in count:
            total_subarrays += count[curr_sum - sum]
        if curr_sum not in count:
            count[curr_sum] = 0
        count[curr_sum] += 1
    return total_subarrays

print(binarySubarrayWithSum([1,0,1,0,1], 2))
print(binarySubarrayWithSum([0,0,0,0,0], 0))
print(binarySubarrayWithSum([1,1,1,1,1], 3))
