# 3 Sum Problem: Find triplets that add upto 0
def three_sum_problem(array):
    n = len(array)
    array.sort()
    result = []

    for i in range(n-2):
        if i != 0 and array[i] == array[i-1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            total = array[i] + array[j] + array[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                result.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
                while j < k and array[j] == array[j-1]:
                    j += 1
                while j < k and array[k] == array[k+1]:
                    k -= 1
        
    return result

array = [-1, 0, 1, 2, -1, -4]
print(three_sum_problem(array))
