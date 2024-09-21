# Longest Repeating Character Replacement
def longestRepeatingCharacterReplacement(s, k):
    l = 0
    char_freq = {}
    longest_str_len = 0
    for r in range(len(s)):
        if s[r] not in char_freq:
            char_freq[s[r]] = 0
        char_freq[s[r]] += 1
        cells_count = r - l + 1
        if cells_count - max(char_freq.values()) <= k:
            longest_str_len = max(longest_str_len, cells_count)
        else:
            char_freq[s[l]] -= 1
            if not char_freq[s[l]]:
                char_freq.pop(s[l])
            l += 1
    return longest_str_len

print(longestRepeatingCharacterReplacement("ABAB", 2))
print(longestRepeatingCharacterReplacement("AABABBA", 1))
print(longestRepeatingCharacterReplacement("ABBB", 2))
print(longestRepeatingCharacterReplacement("A", 0))
