# Capacity to ship packages within D days
def calculate_days(weights, capacity):
    day = 1
    load = 0
    for weight in weights:
        if load + weight > capacity:
            day += 1
            load = weight
        else:
            load += weight
    return day

def least_weight_capacity(weights, days):
    n = len(weights)
    lo = max(weights)
    hi = sum(weights)

    while lo <= hi:
        mid = (lo + hi)//2
        num_days = calculate_days(weights, mid)
        if num_days <= days:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(least_weight_capacity(weights, days))
