# Kadane's Sum: Find the maximum subarray sum in an array
def max_subarray_sum_kadane(array):
    max_sum = array[0]
    current_sum = array[0]
    for i in range(1, len(array)):
        
        current_sum += array[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
        
        if current_sum < 0:
            current_sum = 0

    return max_sum

array = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum_kadane(array))
