# Left Rotate an Array by D places:
def reverse_array(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

def left_rotate_array_by_d_places(array, d):
    n = len(array)
    d = d % n
    reverse_array(array, 0, d - 1)
    reverse_array(array, d, n - 1)
    reverse_array(array, 0, n - 1)
    return array

array = [1, 2, 3, 4, 5]
d = 2
print(left_rotate_array_by_d_places(array, d))
