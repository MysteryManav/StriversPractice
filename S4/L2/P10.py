# Split Array - Largest Sum
def create_partitions(array, max_sum):
    n = len(array)
    elements = 1
    sum = 0
    for num in array:
        if sum + num > max_sum:
            elements += 1
            sum = num
        else:
            sum += num
    return elements

def split_array(array, k):
    n = len(array)
    lo = max(array)
    hi = sum(array)

    while lo <= hi:
        mid = (lo + hi)//2
        partitions = create_partitions(array, mid)
        if partitions > k:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

array = [7, 2, 5, 10, 8]
k = 2
print(split_array(array, k))
