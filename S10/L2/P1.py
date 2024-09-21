# Longest Substring with at most K Distinct Characters
def longestSubstringKDistinct(s, k):
    if k == 0:
        return 0
    start = 0
    end = 0
    max_length = 0
    char_count = {}
    while start <= end:
        if s[end] not in char_count:
            char_count[s[end]] = 1
        else:
            char_count[s[end]] += 1
        if len(char_count) <= k:
            max_length = max(max_length, end - start + 1)
            end += 1
            if end == len(s):
                break
        else:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1
    return max_length

print(longestSubstringKDistinct("aaabbccd", 2))
print(longestSubstringKDistinct("aaabbccd", 3))
print(longestSubstringKDistinct("aaabbccd", 4))
print(longestSubstringKDistinct("aaabbccd", 0))
print(longestSubstringKDistinct("dccbbaaa", 2))
