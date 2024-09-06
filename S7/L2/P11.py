# Combination Sum - 2
def combinationSum(index, target, total, ds=[]):
    if len(ds) == k:
        if total == target:
            ans.append(ds[:])
        return
    
    for i in range(index, 10):
        current = total + i
        if current <= target:
            combinationSum(i+1, target, current, ds+[i])

k = 3
target = 7
ans = []
ds = []
combinationSum(1, target, 0)
print(ans)
