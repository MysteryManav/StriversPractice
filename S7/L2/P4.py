# Better String: String with more number of distinct characters
def subSequences(s, index, output, subSequences=0):
    if index == len(s):
        subSequences += 1
        return subSequences
    
    output = subSequences(s, index+1, output+s[index], subSequences)
    output = subSequences(s, index+1, output, subSequences)

def betterString(s1, s2):
    return s1 if len(set(s1)) > len(set(s2)) else s2

s1 = 'gfg'
s2 = 'ggg'
print(betterString(s1, s2))
