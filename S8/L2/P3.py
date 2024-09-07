# Power Set
def powerSet(s):
    n = len(s)
    result = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(s[j])
        result.append(subset)
    return result

print(powerSet([1, 2, 3]))
print(powerSet([1, 2, 3, 4]))
print(powerSet([1, 2, 3, 4, 5]))
