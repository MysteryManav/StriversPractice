# 4 Sum Problem: Find quadruplets that add upto a target value
def four_sum_problem(array, target):
    n = len(array)
    array.sort()
    result = []

    for i in range(n-3):
        if i > 0 and array[i] == array[i-1]:
            continue

        for j in range(i+1, n-2):
            if j > i+1 and array[j] == array[j-1]:
                continue

            k = j + 1
            l = n - 1
            while k < l:
                total = array[i] + array[j] + array[k] + array[l]
                if total < target:
                    k += 1
                elif total > target:
                    l -= 1
                else:
                    result.append([array[i], array[j], array[k], array[l]])
                    k += 1
                    l -= 1
                    while k < l and array[k] == array[k-1]:
                        k += 1
                    while k < l and array[l] == array[l+1]:
                        l -= 1
    return result

array = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
print(four_sum_problem(array, target))
