# Longest Common Prefix
def longestCommonPrefix(strs):
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    ans = ""

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans

print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["ab", "a"]))
print(longestCommonPrefix(["a", "b"]))
