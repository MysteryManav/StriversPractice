# Combination Sum - 1
def combinationSum(ss, target, index):
    if index == len(ss):
        if target == 0:
            answer.append(ds[:])
        return []
    
    if ss[index] <= target:
        ds.append(ss[index])
        combinationSum(ss, target-ss[index], index)
        ds.pop()
    combinationSum(ss, target, index+1)
    return answer

answer = []
ds = []
ss = [2, 3, 6, 7]
target = 7
print(combinationSum(ss, target, 0))
