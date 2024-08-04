# Koko Eating Bananas: https://leetcode.com/problems/koko-eating-bananas/
import math

def hours_spent_eating(bananas, hour):
    total_hours = 0
    for banana in bananas:
        total_hours += math.ceil(banana/hour)
    return total_hours

def min_eating_speed(bananas, h):
    lo = 1
    hi = max(bananas)

    while lo <= hi:
        mid = (lo + hi)//2
        hours_spent = hours_spent_eating(bananas, mid)
        if hours_spent <= h:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

print(min_eating_speed([3, 6, 7, 11], 8))
print(min_eating_speed([30, 11, 23, 4, 20], 5))
