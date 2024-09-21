# Length of Longest Subsequence without any Repeating Character
def longestSubsequenceWithoutRepeat(string):
    n = len(string)
    occurences = [-1] * 128
    left = 0
    right = 0
    length = 0
    while right < n:
        if occurences[ord(string[right])] != -1:
            left = max(left, occurences[ord(string[right])] + 1)
        occurences[ord(string[right])] = right
        length = max(length, right - left + 1)
        right += 1
    return length

print(longestSubsequenceWithoutRepeat("abcabcbb"))
print(longestSubsequenceWithoutRepeat("bbbbb"))
print(longestSubsequenceWithoutRepeat("pwwkew"))
print(longestSubsequenceWithoutRepeat(" "))
