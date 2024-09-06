# Subset Sum - 2: All unique subsets
def findSubsets(index):
    ans.append(ds[:])
    for i in range(index, len(ss)):
        if i != index and ss[i] == ss[i-1]:
            continue
        ds.append(ss[i])
        findSubsets(i+1 )
        ds.pop()

ans = []
ds = []
ss = [1, 2, 3]
findSubsets(0)
print(ans)
