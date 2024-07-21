# Find the Union of two sorted arrays
def union_of_arrays(arr_1, arr_2):
    n = len(arr_1)
    m = len(arr_2)
    i = j = 0
    union = []
    while i < n and j < m:
        if arr_1[i] < arr_2[j]:
            if len(union) == 0 or union[-1] != arr_1[i]:
                union.append(arr_1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != arr_2[j]:
                union.append(arr_2[j])
            j += 1
    while i < n:
        if len(union) == 0 or union[-1] != arr_1[i]:
            union.append(arr_1[i])
        i += 1
    while j < m:
        if len(union) == 0 or union[-1] != arr_2[j]:
            union.append(arr_2[j])
        j += 1
    return union

arr_1 = [1, 2, 3, 4, 5]
arr_2 = [2, 3, 4, 5, 6]
print(union_of_arrays(arr_1, arr_2))
