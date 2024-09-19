# Number of Next Greater Elements to right
def noOfNextGreaterElement(arr, ind):
    count = 0
    N = len(arr)
    i = ind + 1
    while i < N:
        if arr[i] > arr[ind]:
            count += 1
        i += 1
    return count

print(noOfNextGreaterElement([4, 5, 2, 10, 8], 0))
print(noOfNextGreaterElement([4, 5, 2, 10, 8], 1))
print(noOfNextGreaterElement([4, 5, 2, 10, 8], 2))
print(noOfNextGreaterElement([4, 5, 2, 10, 8], 3))
print(noOfNextGreaterElement([4, 5, 2, 10, 8], 4))
print(noOfNextGreaterElement([3, 2, 1], 0))
