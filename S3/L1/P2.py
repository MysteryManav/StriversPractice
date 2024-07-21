# Find Second Smallest and Second Largest Element in an Array without sorting
def second_smallest_element(array):
    if len(array) < 2:
        return "Invalid Input"
    smallest = second_smallest = float('inf')
    for i in range(len(array)):
        if array[i] < smallest:
            second_smallest = smallest
            smallest = array[i]
        elif array[i] < second_smallest and array[i] != smallest:
            second_smallest = array[i]
    return second_smallest

def second_largest_element(array):
    if len(array) < 2:
        return "Invalid Input"
    largest = second_largest = float('-inf')
    for i in range(len(array)):
        if array[i] > largest:
            second_largest = largest
            largest = array[i]
        elif array[i] > second_largest and array[i] != largest:
            second_largest = array[i]
    return second_largest

array = [12, 34, 45, 9, 8, 90, 3]
print(second_smallest_element(array))
print(second_largest_element(array))
