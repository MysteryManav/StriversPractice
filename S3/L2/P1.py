# Two Sum: Check if a pair with given sum exists
def merge(array, low, mid, high):
    temp_arr = []
    left = low
    right = mid+1
    while left <= mid and right <= high:
        if array[left] <= array[right]:
            temp_arr.append(array[left])
            left += 1
        else:
            temp_arr.append(array[right])
            right += 1
    while left <= mid:
        temp_arr.append(array[left])
        left += 1
    while right <= high:
        temp_arr.append(array[right])
        right += 1
    for i in range(low, high+1):
        array[i] = temp_arr[i-low]

def merge_sort(array, low, high):
    if low >= high:
        return
    mid = (low + high)//2
    merge_sort(array, low, mid)
    merge_sort(array, mid+1, high)
    merge(array, low, mid, high)

def two_sum_check(array, k):
    merge_sort(array, 0, len(array)-1)
    n = len(array)
    left = 0
    right = n - 1
    while left < right:
        if array[left] + array[right] == k:
            print("YES")
            return [left, right]
        elif array[left] + array[right] < k:
            left += 1
        else:
            right -= 1
    print("NO")
    return [-1, -1]

array = [3, 4, 2, 1, 5, 0]
k = 7
print(two_sum_check(array, k))
