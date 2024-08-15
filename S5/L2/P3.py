# Roman to Integer
def romanToInt(s):
    romanVals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s) - 1):
        if romanVals[s[i]] < romanVals[s[i+1]]:
            result -= romanVals[s[i]]
        else:
            result += romanVals[s[i]]
    return result + romanVals[s[-1]]

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
