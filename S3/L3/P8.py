# Merge two sorted arrays without extra space
def swap_elements_if_greater(arr_1, arr_2, i, j):
    if arr_1[i] > arr_2[j]:
        arr_1[i], arr_2[j] = arr_2[j], arr_1[i]

def merge_sorted_arrays(arr_1, arr_2):
    n = len(arr_1)
    m = len(arr_2)
    tot_len = n + m
    
    gap = (tot_len) // 2 + (tot_len) % 2

    while gap > 0:
        left = 0
        right = left + gap
        while right < tot_len:
            if left < n and right >= n:
                swap_elements_if_greater(arr_1, arr_2, left, right - n)
            elif left >= n:
                swap_elements_if_greater(arr_2, arr_2, left - n, right - n)
            else:
                swap_elements_if_greater(arr_1, arr_1, left, right)
            left += 1
            right += 1
        if gap == 1:
            break
        gap = gap // 2 + gap % 2

    return arr_1, arr_2

arr_1 = [1, 3, 5, 7]
arr_2 = [0, 2, 6, 8, 9]
print(merge_sorted_arrays(arr_1, arr_2))                
