# Number of substrings containing all three characters
def substringsContainingThreeCharacters(s):
    n = len(s)
    lastSeen = [-1] * 3
    count = 0
    for i in range(n):
        lastSeen[ord(s[i]) - ord('a')] = i
        if min(lastSeen) != -1:
            count += min(lastSeen) + 1
    return count

print(substringsContainingThreeCharacters("abcabc"))
print(substringsContainingThreeCharacters("aaacb"))
print(substringsContainingThreeCharacters("abc"))
