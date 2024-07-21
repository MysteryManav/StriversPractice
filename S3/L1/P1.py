# Largest Element in an Array
def largest_element_in_array(array):
    largest_element = array[0]
    for i in range(1, len(array)):
        if array[i] > largest_element:
            largest_element = array[i]
    return largest_element

array = [12, 34, 45, 9, 8, 90, 3]
print(largest_element_in_array(array))
