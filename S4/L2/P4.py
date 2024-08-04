# Minimum days to make M banquets
def possible(array, day, rose, bouqets):
    n = len(array)
    count = 0
    no_of_bouqets = 0
    for i in range(n):
        if array[i] <= day:
            count += 1
        else:
            no_of_bouqets += count//rose
            count = 0
    no_of_bouqets += count//rose
    return no_of_bouqets >= bouqets

def rose_garden(array, roses, bouqets):
    val = roses * bouqets
    n = len(array)
    lo = min(array)
    hi = max(array)

    while lo <= hi:
        mid = (lo + hi)//2
        if possible(array, mid, roses, bouqets):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

print(rose_garden([1, 2, 4, 9], 2, 2))
print(rose_garden([1, 4, 8, 5], 2, 2))
print(rose_garden([7, 7, 7, 7, 13, 11, 12, 7], 3, 2))
