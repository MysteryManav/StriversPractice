# Generate all Binary Strings
def allBinaryStrings(n, arr, i):
    if i == n:
        print(*arr[:n], sep='', end=' ')
        return
    if arr[i-1] == '1':
        arr[i] = '0'
        allBinaryStrings(n, arr, i+1)
    if arr[i-1] == '0':
        arr[i] = '0'
        allBinaryStrings(n, arr, i+1)
        arr[i] = '1'
        allBinaryStrings(n, arr, i+1)

def generateAllBinaryStrings(n):
    if n <= 0:
        return
    arr = ['0']*n 

    arr[0] = '0'
    allBinaryStrings(n, arr, 1)

    arr[0] = '1'
    allBinaryStrings(n, arr, 1)
    
generateAllBinaryStrings(3)
print()
