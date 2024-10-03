# Merge K Sorted Arrays

def mergeTwoSortedArrays(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    i, j = 0, 0
    result = []
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < n1:
        result.append(arr1[i])
        i += 1
    while j < n2:
        result.append(arr2[j])
        j += 1
    return result

def mergeKSortedArrays(arrays):
    n = len(arrays)
    if n == 0:
        return []
    if n == 1:
        return arrays[0]
    if n == 2:
        return mergeTwoSortedArrays(arrays[0], arrays[1])
    mid = n // 2
    left = mergeKSortedArrays(arrays[:mid])
    right = mergeKSortedArrays(arrays[mid:])
    return mergeTwoSortedArrays(left, right)

print(mergeKSortedArrays([[1, 3, 5], [2, 4, 6], [0, 9, 10]]))
print(mergeKSortedArrays([[1, 3, 5], [2, 4, 6], [0, 9, 10], [7, 8, 11]]))
print(mergeKSortedArrays([[1, 3, 5], [2, 4, 6], [0, 9, 10], [7, 8, 11], [12, 13, 14]]))
