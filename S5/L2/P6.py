# Longest Palindromic Substring (without DP)
def longest_palindromic_substring(s):
    if len(s) <= 1:
        return s
    max_str = s[0]

    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    for i in range(len(s)):
        odd = expandAroundCenter(i, i)
        even = expandAroundCenter(i, i+1)
        if len(odd) > len(max_str):
            max_str = odd
        if len(even) > len(max_str):
            max_str = even
    return max_str

print(longest_palindromic_substring("babad"))
print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("a"))
