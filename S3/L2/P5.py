# Kadane's Sum: Find the maximum subarray sum in an array and also print the subarray
def max_subarray_sum_kadane(array):
    max_sum = array[0]
    current_sum = array[0]
    max_sum_start = 0
    max_sum_end = 0
    current_sum_start = 0
    for i in range(1, len(array)):
        if current_sum == 0:
            current_sum_start = i
        
        current_sum += array[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_start = current_sum_start
            max_sum_end = i
        
        if current_sum < 0:
            current_sum = 0
    
    for i in range(max_sum_start, max_sum_end+1):
        print(array[i], end=" ")
    print()
    return max_sum

array = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum_kadane(array))
