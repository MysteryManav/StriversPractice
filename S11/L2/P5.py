# Replace elements by its rank in the array
def replaceElements(arr):
    n = len(arr)
    temp = arr.copy()
    rank = {}
    temp.sort()
    for i in range(n):
        if temp[i] not in rank:
            rank[temp[i]] = i+1
    for i in range(n):
        arr[i] = rank[arr[i]]
    return arr

print(replaceElements([10, 8, 15, 12, 6, 20, 1]))
print(replaceElements([1, 2, 3, 4, 5, 6, 7]))
