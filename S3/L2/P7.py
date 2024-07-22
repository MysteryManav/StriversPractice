# Rearrange array elements by sign: Without altering relative order rearrange them in alternaing positive and negative
def rearrange_positive_negative(array):
    n = len(array)
    positive = 0
    negative = 1

    rearranged_array = [0] * n
    for i in range(n):
        if array[i] >= 0:
            rearranged_array[positive] = array[i]
            positive += 2
        elif array[i] < 0:
            rearranged_array[negative] = array[i]
            negative += 2
    return rearranged_array

# Array with equal positives and negatives
array = [1, 2, 3, -1, -2, -3]
print(rearrange_positive_negative(array))
