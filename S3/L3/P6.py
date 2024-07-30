# Count number of subarrays with given xor k
def subarrays_with_xor_k(array, k):
    n = len(array)
    xr = 0
    count = 0
    xor_map = {}
    xor_map[0] = 1
    for i in range(n):
        xr ^= array[i]
        x = xr ^ k
        count += xor_map.get(x, 0)
        xor_map[xr] = xor_map.get(xr, 0) + 1
    return count

array = [4, 2, 2, 6, 4]
k = 6
print(subarrays_with_xor_k(array, k))
