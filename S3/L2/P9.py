# Print Leaders in an Array
def leaders_in_array(array):
    n = len(array)

    max_element = array[-1]
    leaders = [max_element]

    for i in range(n-1, -1, -1):
        if array[i] > max_element:
            max_element = array[i]
            leaders.append(max_element)
    
    return leaders[::-1]

array = [16, 17, 4, 3, 5, 2]
print(leaders_in_array(array))
