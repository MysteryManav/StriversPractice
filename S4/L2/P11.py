# Painter's Partition Problem
def can_allocate_painters(boards, time):
    painters_required = 1
    time_allocated = 0
    for board in boards:
        if time_allocated + board > time:
            painters_required += 1
            time_allocated = board
        else:
            time_allocated += board
    return painters_required

def painters_partition(boards, painters):
    lo = max(boards)
    hi = sum(boards)

    while lo <= hi:
        mid = (lo + hi)//2
        painters_allocated = can_allocate_painters(boards, mid)
        if painters_allocated > painters:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

boards = [10, 20, 30, 40]
painters = 2
print(painters_partition(boards, painters))
