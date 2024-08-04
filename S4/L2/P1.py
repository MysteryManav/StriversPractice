# Find Square Root of a number using Binary Search
def square_root(num):
    lo = 0
    hi = num

    while lo <= hi:
        mid = (lo + hi)//2
        val = mid * mid
        if val == num:
            return mid
        elif val < num:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return hi

print(square_root(16))
print(square_root(17))
