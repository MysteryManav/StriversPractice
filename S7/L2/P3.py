# Power Set: Print all Possible Subsequences of String
def printPossibleString(s, index, output):
    if index == len(s):
        print(output, end=' ')
        return
    
    printPossibleString(s, index+1, output+s[index])
    printPossibleString(s, index+1, output)

s = 'abc'
printPossibleString(s, 0, '')
