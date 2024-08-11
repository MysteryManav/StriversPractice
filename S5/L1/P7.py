# Check if two strings are anagrams of each other
def check_anagrams(s, t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    return s == t

print(check_anagrams("anagram", "nagaram"))
print(check_anagrams("rat", "car"))
print(check_anagrams("a", "ab"))
