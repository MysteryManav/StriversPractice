# Find the majority element that occurs more than n/2 times in a list of n elements
# Using Moore's Voting Algorithm
def majority_elemtn_moore(array):
    element_count = 0
    element = None
    for i in range(len(array)):
        if element_count == 0:
            element = array[i]
            element_count = 1
        elif element == array[i]:
            element_count += 1
        elif element != array[i]:
            element_count -= 1
    return element

array = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1]
print(majority_elemtn_moore(array))
