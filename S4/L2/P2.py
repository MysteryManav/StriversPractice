# N-th root of a number using Binary Search
def check_nth_root(mid, n, m):
    val = 1
    for i in range(1, n+1):
        val *= mid
        if val > m:
            return 2
    if val == m:
        return 1
    return 0

def nth_root_using_binary_search(n, m):
    lo = 1
    hi = m
    while lo <= hi:
        mid = (lo + hi)//2
        val = check_nth_root(mid, n, m)
        if val == 1:
            return mid
        elif val == 0:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

print(nth_root_using_binary_search(2, 16))
print(nth_root_using_binary_search(3, 27))
