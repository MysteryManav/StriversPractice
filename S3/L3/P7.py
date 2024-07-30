# Merge Overlapping Sub-Intervals
def merge_overlapping_sub_intervals(array):
    n = len(array)
    array.sort(key=lambda x: x[0])
    stack = []
    stack.append(array[0])
    for i in range(1, n):
        top = stack[-1]
        if top[1] < array[i][0]:
            stack.append(array[i])
        elif top[1] > array[i][0]:
            top[1] = max(top[1], array[i][1])
            stack.pop()
            stack.append(top)
    return stack

array = [[1, 3], [8, 10], [2, 6], [15, 18]]
print(merge_overlapping_sub_intervals(array))
