# Maximum Consecutive Ones in an array of 1 and 0
def maximum_consecutive_ones_count(array):
    count = 0
    max_count = 0
    for i in range(len(array)):
        if array[i] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

array = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
print(maximum_consecutive_ones_count(array))
