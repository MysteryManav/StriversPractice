# Majority Element (N/3 Times): Extended Boyer Moore's Voting Algorithm
def extended_moore_voting(array):
    count_1 = 0
    element_1 = None

    count_2 = 0
    element_2 = None

    for i in array:
        if count_1 == 0 and i != element_2:
            element_1 = i
            count_1 = 1
        elif count_2 == 0 and i != element_1:
            element_2 = i
            count_2 = 1
        elif i == element_1:
            count_1 += 1
        elif i == element_2:
            count_2 += 1
        else:
            count_1 -= 1
            count_2 -= 1

    return [[element_1, count_1], [element_2, count_2]]

array = [11, 33, 33, 11, 33, 11]
print(extended_moore_voting(array))
