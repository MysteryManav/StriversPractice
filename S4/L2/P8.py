# Aggressive Cows: Find maximum possible minimum distance between cows/Maximize the minimum distance to be kept between cows
def can_place_cows(stalls, mid, cows):
    n = len(stalls)
    cow_count = 1
    last = stalls[0]
    for i in range(1, n):
        if stalls[i] - last >= mid:
            cow_count += 1
            last = stalls[i]
        if cow_count >= cows:
            return True
    return False

def aggressive_cows(stalls, cows):
    n = len(stalls)
    stalls.sort()
    lo = 1
    hi = stalls[n - 1] - stalls[0]

    while lo <= hi:
        mid = (lo + hi)//2
        if can_place_cows(stalls, mid, cows):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

stalls = [0, 3, 4, 7, 10, 9]
cows = 4
print(aggressive_cows(stalls, cows))
