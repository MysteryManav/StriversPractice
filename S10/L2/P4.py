# Minimum Window Subsequence
def minWindowSubstring(s, t):
    if not s or not t or len(s) < len(t):
        return ""
    
    mpp = [0] * 128
    count = len(t)
    start = 0
    end = 0
    min_length = float('inf')
    start_index = 0
    for c in t:
        mpp[ord(c)] += 1

    while end < len(s):
        if mpp[ord(s[end])] > 0:
            count -= 1
        mpp[ord(s[end])] -= 1
        end += 1
        
        while count == 0:
            if end - start < min_length:
                min_length = end - start
                start_index = start
            mpp[ord(s[start])] += 1
            if mpp[ord(s[start])] > 0:
                count += 1
            start += 1
    return "" if min_length == float('inf') else s[start_index:start_index + min_length]

print(minWindowSubstring("ADOBECODEBANC", "ABC"))
print(minWindowSubstring("a", "a"))
print(minWindowSubstring("a", "aa"))
