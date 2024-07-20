# Merge Sort
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

array = [3, 4, 2, 1, 5, 0]
merge_sort(array, 0, len(array)-1)
print(array)
